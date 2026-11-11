import json

with open('FINAL_gamma_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

gen_qs = [q for q in questions if q['topic'] == 'Genetica e Biologia Molecular']
print(f"Total mapped to Genetica: {len(gen_qs)}")
for q in gen_qs[:10]:
    print(f"{q['edition']} Q{q['question_number']} disc={q['discipline']}: {q['text_snippet'][:120]}")
