import json
from collections import Counter

with open('FINAL_gamma_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

total_q = len(questions)
print(f"Total Questions Analyzed: {total_q}")

# 1. Discipline distribution
disc_counts = Counter(q['discipline'] for q in questions)
print("\n=== DISTRIBUIÇÃO POR DISCIPLINA ===")
for disc, count in disc_counts.most_common():
    pct = (count / total_q) * 100
    print(f"{disc:12s}: {count:5d} ({pct:6.2f}%)")

# 2. Topic distribution per discipline
print("\n=== INCIDÊNCIA POR DISCIPLINA E TÓPICO ===")
disc_topics = {}
for q in questions:
    disc = q['discipline']
    top = q['topic']
    hab = q['habilidade']
    if disc not in disc_topics:
        disc_topics[disc] = {}
    if top not in disc_topics[disc]:
        disc_topics[disc][top] = {'count': 0, 'habilidade': hab}
    disc_topics[disc][top]['count'] += 1

stats_output = {}

for disc in ['Matematica', 'Fisica', 'Quimica', 'Biologia']:
    total_disc = disc_counts[disc]
    print(f"\n--- {disc.upper()} (Total: {total_disc} questões - {total_disc/total_q*100:.2f}%) ---")
    topics = disc_topics[disc]
    sorted_topics = sorted(topics.items(), key=lambda x: x[1]['count'], reverse=True)
    stats_output[disc] = []
    for top, data in sorted_topics:
        cnt = data['count']
        pct_disc = (cnt / total_disc) * 100
        pct_total = (cnt / total_q) * 100
        hab = data['habilidade']
        print(f"  {top:45s}: {cnt:4d} ({pct_disc:5.2f}% da disc | {pct_total:5.2f}% total) | Hab: {hab}")
        stats_output[disc].append({
            'topic': top,
            'count': cnt,
            'pct_disc': round(pct_disc, 2),
            'pct_total': round(pct_total, 2),
            'habilidade': hab
        })

# 3. Interdisciplinary patterns
inter_list = []
for q in questions:
    if q['interdisciplinary']:
        for item in q['interdisciplinary']:
            inter_list.append(item)

inter_counts = Counter(inter_list)
print("\n=== PADRÕES INTERDISCIPLINARES MAIS FREQUENTES ===")
for item, cnt in inter_counts.most_common(15):
    pct = (cnt / total_q) * 100
    print(f"  {item:60s}: {cnt:4d} ({pct:5.2f}%)")

with open('stats_summary_gamma.json', 'w', encoding='utf-8') as f:
    json.dump({
        'total_questions': total_q,
        'discipline_counts': disc_counts,
        'topics': stats_output,
        'interdisciplinary': dict(inter_counts.most_common(20))
    }, f, indent=2, ensure_ascii=False)
print("\nSaved stats summary to stats_summary_gamma.json")
