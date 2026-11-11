import json

with open('FINAL_gamma_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

for q in questions:
    if q['edition'] == '2019_1º conjunto' and q['question_number'] in [91, 92, 93, 94, 95, 98]:
        print(f"=== Q{q['question_number']} ===")
        print(q['text_snippet'][:300])
        print()
