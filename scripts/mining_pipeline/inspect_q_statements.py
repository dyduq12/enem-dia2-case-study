import test_semantic_classifier as tsc

sample_pdf = r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2024\1º\SIMULADO 1 - GABARITO COMENTADO.pdf"
qs = tsc.extract_questions_from_pdf(sample_pdf)

for q in qs[:45]:
    # first 150 chars of statement
    lines = [l.strip() for l in q["text"].split("\n") if l.strip()]
    snippet = " ".join(lines[:3])[:120]
    print(f"Q{q['num']}: {snippet}")
