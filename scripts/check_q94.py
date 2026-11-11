import json

with open('FINAL_gamma_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

for q in questions:
    if q['edition'] == '2019_1º conjunto' and q['question_number'] == 94:
        print("Edition:", q['edition'], "Q:", q['question_number'])
        print("Discipline:", q['discipline'])
        print("Topic:", q['topic'])
