import os
from datetime import datetime

dir1 = "folder1"
dir2 = "folder2"
output = "result.txt"

files1 = set(os.listdir(dir1))
files2 = set(os.listdir(dir2))

same = files1 & files2

with open(output, "w", encoding="utf-8") as out:
    for fname in same:
        file1 = os.path.join(dir1, fname)
        file2 = os.path.join(dir2, fname)

        t1 = os.path.getctime(file1)
        t2 = os.path.getctime(file2)

        if t1 == t2:
            continue
        if t1 > t2:
            newer = " 1"
            diff = t1 - t2
        else:
            newer = " 2"
            diff = t2 - t1

        diff = round(diff, 2)

        out.write(f"{fname}: {newer}, пізніше на {diff} секунд\n")

