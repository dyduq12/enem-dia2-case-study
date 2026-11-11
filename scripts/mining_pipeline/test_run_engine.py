import test_semantic_classifier as tsc
import semantic_engine as se
from collections import Counter

sample_pdf = r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2024\1º\SIMULADO 1 - GABARITO COMENTADO.pdf"
qs = tsc.extract_questions_from_pdf(sample_pdf)

classified_qs = []
disc_counter = Counter()
topic_counter = Counter()

for q in qs:
    res = se.classify_question(q["num"], q["text"])
    disc_counter[res["discipline"]] += 1
    topic_counter[(res["discipline"], res["topic"])] += 1
    classified_qs.append({
        "num": q["num"],
        "discipline": res["discipline"],
        "topic": res["topic"],
        "skill": res["skill"],
        "interdisc": res["interdisciplinary"]
    })

print(f"Sample breakdown for {len(qs)} questions:")
print("\nDisciplines:")
for d, cnt in disc_counter.most_common():
    print(f"  {d}: {cnt} ({cnt/len(qs)*100:.1f}%)")

print("\nTop 15 Topics:")
for (d, top), cnt in topic_counter.most_common(15):
    print(f"  [{d}] {top}: {cnt}")
