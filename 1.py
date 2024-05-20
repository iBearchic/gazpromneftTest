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
