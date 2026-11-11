import json
import re

with open('text_stats.json', 'r', encoding='utf-8') as f:
    stats = json.load(f)

stats.sort(key=lambda x: x.get('total_chars', 0), reverse=True)

with_text = [s for s in stats if s.get('total_chars', 0) >= 500]
print(f"Total candidates: {len(stats)}")
print(f"Candidates with substantial text: {len(with_text)}")

print("\nSample top files:")
for s in with_text[:15]:
    print(f"{s['pages']:3d} pgs | {s['total_chars']:7d} chars | {s['filename']}")

print("\nSample files near cutoff:")
for s in with_text[-15:]:
    print(f"{s['pages']:3d} pgs | {s['total_chars']:7d} chars | {s['filename']}")
