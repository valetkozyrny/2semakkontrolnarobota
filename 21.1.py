import re

def fix_dates(text):
    def repl_dot(m):
        d, mth, y = m.groups()
        return f"{int(d):02d}.{int(mth):02d}.{y}"

    text = re.sub(r'\b(\d{1,2})\.(\d{1,2})\.(\d{4})\b', repl_dot, text)

    def repl_slash(m):
        y, mth, d = m.groups()
        return f"{int(d):02d}.{int(mth):02d}.{y}"

    text = re.sub(r'\b(\d{4})/(\d{1,2})/(\d{1,2})\b', repl_slash, text)

    return text



input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r", encoding="utf-8") as f:
    data = f.read()

new_data = fix_dates(data)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(new_data)

