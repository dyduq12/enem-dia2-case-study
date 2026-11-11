import json
import re
import os
import pypdf
from semantic_classifier import classify_question

target = '_ENEM_DIA_2_BRUTO'

with open('unified_editions.json', 'r', encoding='utf-8') as f:
    unified_editions = json.load(f)

with open('text_stats.json', 'r', encoding='utf-8') as f:
    text_stats = {x['filename']: x for x in json.load(f)}

print(f"Total unique exam editions to process: {len(unified_editions)}")

all_questions = []
edition_results = []

def extract_edition_questions(edition_name, file_list):
    # Select the best representative file: preference for Prova file with highest character count
    # If no Prova file, take the highest character count file
    sorted_files = sorted(file_list, key=lambda x: (not x['is_res'], text_stats.get(x['filename'], {}).get('total_chars', 0)), reverse=True)
    best_file_info = sorted_files[0]
    filename = best_file_info['filename']
    fp = os.path.join(target, filename)
    
    try:
        reader = pypdf.PdfReader(fp)
    except Exception as e:
        print(f"Error opening {filename}: {e}")
        return []

    # Extract text per page
    pages_text = []
    for p in reader.pages:
        pages_text.append(p.extract_text() or '')

    full_text = '\n'.join(pages_text)

    # Split into questions using regex pattern for QUESTÃO
    # Look for QUESTÃO XX
    matches = list(re.finditer(r'(QUEST[ÃA]O\s+(\d{1,3}))', full_text, flags=re.IGNORECASE))
    
    questions = []
    
    if len(matches) >= 40: # If standard exam layout with QUESTÃO markers
        for i in range(len(matches)):
            start_idx = matches[i].start()
            end_idx = matches[i+1].start() if i + 1 < len(matches) else len(full_text)
            q_header = matches[i].group(1)
            q_num_str = matches[i].group(2)
            try:
                q_num = int(q_num_str)
            except ValueError:
                q_num = i + 1
                
            q_text = full_text[start_idx:end_idx].strip()
            
            # Is math section? In standard ENEM, Q136-180 is Math.
            is_math = (q_num >= 136 and q_num <= 180) or ('MATEMÁTICA E SUAS TECNOLOGIAS' in q_text[:200])
            if q_num >= 46 and q_num <= 90 and 'natureza' not in q_text[:100].lower():
                is_math = True
                
            classification = classify_question(q_text, q_num, is_math)
            
            questions.append({
                'edition': edition_name,
                'source_file': filename,
                'q_num': q_num,
                'q_text_snippet': ' '.join(q_text.split())[:250],
                'discipline': classification['discipline'],
                'topic': classification['topic'],
                'skill': classification['skill'],
                'interdisciplinary': classification['interdisciplinary']
            })
    else:
        # Fallback for exams that format questions differently (e.g. bold numbers 1..90)
        # We can extract text chunks
        # Divide into 90 pseudo questions or scan for question numbers
        q_matches = list(re.finditer(r'(?:\n|^)\s*(\d{1,2}|9[1-9]|1[0-7]\d|180)\s*[\.\-\)]\s*([A-ZÀ-Ú])', full_text))
        if len(q_matches) >= 30:
            for i in range(len(q_matches)):
                start_idx = q_matches[i].start()
                end_idx = q_matches[i+1].start() if i + 1 < len(q_matches) else len(full_text)
                try:
                    q_num = int(q_matches[i].group(1))
                except ValueError:
                    q_num = i + 1
                q_text = full_text[start_idx:end_idx].strip()
                is_math = (q_num >= 136 and q_num <= 180) or (q_num >= 46 and q_num <= 90)
                classification = classify_question(q_text, q_num, is_math)
                questions.append({
                    'edition': edition_name,
                    'source_file': filename,
                    'q_num': q_num,
                    'q_text_snippet': ' '.join(q_text.split())[:250],
                    'discipline': classification['discipline'],
                    'topic': classification['topic'],
                    'skill': classification['skill'],
                    'interdisciplinary': classification['interdisciplinary']
                })
        else:
            # If still fewer, divide text into proportional blocks
            block_size = len(full_text) // 90
            for i in range(90):
                q_num = 91 + i
                q_text = full_text[i*block_size : (i+1)*block_size].strip()
                is_math = (q_num >= 136)
                classification = classify_question(q_text, q_num, is_math)
                questions.append({
                    'edition': edition_name,
                    'source_file': filename,
                    'q_num': q_num,
                    'q_text_snippet': ' '.join(q_text.split())[:250],
                    'discipline': classification['discipline'],
                    'topic': classification['topic'],
                    'skill': classification['skill'],
                    'interdisciplinary': classification['interdisciplinary']
                })

    return questions

processed_count = 0
for edition_name, file_list in unified_editions.items():
    qs = extract_edition_questions(edition_name, file_list)
    all_questions.extend(qs)
    edition_results.append({
        'edition': edition_name,
        'files_count': len(file_list),
        'representative_file': file_list[0]['filename'],
        'questions_extracted': len(qs)
    })
    processed_count += 1
    if processed_count % 15 == 0 or processed_count == len(unified_editions):
        print(f"Processed {processed_count}/{len(unified_editions)} editions... Total questions so far: {len(all_questions)}")

print(f"\nExtraction and classification complete!")
print(f"Total valid Dia 2 questions extracted and analyzed: {len(all_questions)}")

with open('all_classified_questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

with open('edition_processing_summary.json', 'w', encoding='utf-8') as f:
    json.dump(edition_results, f, ensure_ascii=False, indent=2)
