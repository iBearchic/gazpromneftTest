# имеется текстовый файл file.csv, в котром разделитель полей с данными: | (верт. черта)
# пример ниже содержит небольшую часть этого файла(начальные 3 строки, включая строку заголовков полей)

"""
lastname|name|patronymic|date_of_birth|id
Фамилия1|Имя1|Отчество1 |21.11.1998   |312040348-3048
Фамилия2|Имя2|Отчество2 |11.01.1972   |457865234-3431
...
"""

# Задание
# 1. Реализовать сбор уникальных записей
# 2. Случается, что под одиннаковым id присутствуют разные данные - собрать отдельно такие записи


import csv
from collections import defaultdict

with open('file.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    records = [row for row in reader]

# Сбор уникальных записей
# Группировка записей c различными данными по одинаковому id

unique_records = {}
record_groups = defaultdict(list)
for row in records:
    record_groups[row['id']].append(row)

for row_id in record_groups:
  if len(record_groups[row_id]) == 1:
    unique_records[row_id] = record_groups[row_id][0]

print(f"Уникальные записи: {list(unique_records.values())}")
print(f"Записи с одинаковым id: {[val for key, val in record_groups.items() if len(val) > 1]}")
