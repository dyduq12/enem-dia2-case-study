import test_semantic_classifier as tsc
import semantic_engine as se

sample_pdf = r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2024\1º\SIMULADO 1 - GABARITO COMENTADO.pdf"
qs = tsc.extract_questions_from_pdf(sample_pdf)

for q in qs[:45]:
    res = se.classify_question(q["num"], q["text"])
    if res["topic"] == "Genética e Biotecnologia":
        # find which keyword matched
        matched = []
        for _, kws, _ in se.BIOLOGY_TOPICS:
            for kw in kws:
                if kw in q["text"].lower():
                    matched.append(kw)
        print(f"Q{q['num']}: matched {matched}")
