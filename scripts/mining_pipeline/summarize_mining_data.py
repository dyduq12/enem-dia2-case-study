import json

with open("delta_mining_results.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total Questions: {data['total_questions']}")
print("\nDiscipline breakdown:")
for d, cnt in data["discipline_counts"].items():
    print(f"  {d}: {cnt} ({cnt/data['total_questions']*100:.2f}%)")

for disc in ["Matemática", "Física", "Química", "Biologia"]:
    print(f"\n==================== {disc.upper()} ====================")
    topics = data["discipline_topics"].get(disc, {})
    total_disc = data["discipline_counts"].get(disc, 1)
    sorted_topics = sorted(topics.items(), key=lambda x: x[1], reverse=True)
    for top, cnt in sorted_topics:
        pct_disc = (cnt / total_disc) * 100
        pct_total = (cnt / data["total_questions"]) * 100
        # skills
        skills = data["topic_skills_map"].get(top, {})
        sk_str = ", ".join(f"{k} ({v})" for k, v in sorted(skills.items(), key=lambda x: x[1], reverse=True)[:3])
        print(f"  {top:60} | {cnt:4} ({pct_disc:5.1f}% disc, {pct_total:4.1f}% tot) | Skills: {sk_str}")

print("\nInterdisciplinary Patterns:")
for pattern, cnt in sorted(data["interdisciplinary_counts"].items(), key=lambda x: x[1], reverse=True):
    print(f"  {pattern:60}: {cnt}")
