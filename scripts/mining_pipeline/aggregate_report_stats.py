import json
from collections import Counter

with open('all_classified_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

total_q = len(questions)
print(f"Total Questions Analyzed: {total_q}")

# Discipline stats
disc_counts = Counter(q['discipline'] for q in questions)
print("\n--- DISTRIBUIÇÃO POR DISCIPLINA ---")
for disc, count in disc_counts.most_common():
    pct = (count / total_q) * 100
    print(f"{disc}: {count} ({pct:.2f}%)")

# Topic stats per discipline
print("\n--- TOPICOS POR DISCIPLINA ---")
disc_topics = {}
for q in questions:
    disc = q['discipline']
    topic = q['topic']
    disc_topics.setdefault(disc, []).append((topic, q['skill']))

topic_stats = {}
for disc, items in disc_topics.items():
    cnt = Counter(x[0] for x in items)
    skill_map = {x[0]: x[1] for x in items}
    disc_total = len(items)
    topic_stats[disc] = []
    print(f"\nDiscipline: {disc} (Total: {disc_total})")
    for top, c in cnt.most_common():
        pct_disc = (c / disc_total) * 100
        pct_total = (c / total_q) * 100
        print(f"  - {top}: {c} ({pct_disc:.2f}% da disciplina, {pct_total:.2f}% do total)")
        topic_stats[disc].append({
            'topic': top,
            'count': c,
            'pct_discipline': round(pct_disc, 2),
            'pct_total': round(pct_total, 2),
            'typical_skill': skill_map.get(top, '')
        })

# Interdisciplinary patterns
inter_items = [q for q in questions if q.get('interdisciplinary')]
inter_counts = Counter(q['interdisciplinary'] for q in inter_items)

print(f"\n--- PADRÕES INTERDISCIPLINARES (Total: {len(inter_items)} questões, {len(inter_items)/total_q*100:.2f}%) ---")
inter_stats = []
for pattern, count in inter_counts.most_common():
    pct = (count / total_q) * 100
    print(f"  - {pattern}: {count} ({pct:.2f}%)")
    inter_stats.append({
        'pattern': pattern,
        'count': count,
        'pct_total': round(pct, 2)
    })

results = {
    'total_questions': total_q,
    'disciplines': {disc: {'count': count, 'pct': round((count/total_q)*100, 2)} for disc, count in disc_counts.items()},
    'topics_by_discipline': topic_stats,
    'interdisciplinary': {
        'total_count': len(inter_items),
        'pct_total': round((len(inter_items)/total_q)*100, 2),
        'patterns': inter_stats
    }
}

with open('aggregated_report_stats.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nAggregated stats saved to aggregated_report_stats.json")
