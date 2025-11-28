import re

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

sentences = re.split(r'(?<=[.!?])\s+', text)

with open("output.txt", "w", encoding="utf-8") as f:
    for s in sentences:
        f.write(s.strip() + "\n")

