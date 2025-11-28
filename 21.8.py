import re

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

text = re.sub(r'(?<!\d)\.(\d+)', r'0.\1', text)
text = re.sub(r'(\d+)\.(?!\d)', r'\1.0', text)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

