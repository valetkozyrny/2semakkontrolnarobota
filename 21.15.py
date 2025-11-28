import re

template = """
<Адреса>
Шановна(ий) {name}
Сума Вашого боргу за послуги складає {debt}.
Просимо сплатити борг протягом місяця. У іншому випадку, надання послуг буде припинено.
"""

def parse(line):
    line = line.strip()

    addr = re.search(r'(адрес[^\s:]*[:.]?\s*.*?)(тел|[0-9]|$)', line, re.I)
    address = addr.group(1).strip() if addr else "Адреса не знайдена"

    phone = re.search(r'(телефон|тел)[^\d]*([\d\-\+\s]{6,})', line, re.I)
    phone = phone.group(2).strip() if phone else "Немає телефону"

    debt = re.findall(r'\d+[\.,]?\d*', line)
    debt = debt[-1] if debt else "0"

    name_part = re.split(r'(адрес|тел)', line, flags=re.I)[0]
    name = name_part.strip()

    return address, name, debt, phone


with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("mails.txt", "w", encoding="utf-8") as f:
    for line in lines:
        address, name, debt, phone = parse(line)
        letter = template.format(name=name, debt=debt)
        letter = letter.replace("<Адреса>", address + "\nТелефон: " + phone)
        f.write(letter + "\n" + "-"*40 + "\n")

