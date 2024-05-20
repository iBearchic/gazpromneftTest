# в наличии список множеств. внутри множества целые числа
m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

# Задание: посчитать 
#  1. общее количество чисел
#  2. общую сумму чисел
#  3. посчитать среднее значение
#  4. собрать все множества в один кортеж
# *написать решения в одну строку

total_count = sum(len(s) for s in m)
total_sum = sum(sum(s) for s in m)
average = total_sum / total_count
combined_tuple = tuple(num for s in m for num in s)

print(f"Общее количество чисел: {total_count}")
print(f"Общая сумма чисел: {total_sum}")
print(f"Среднее значение: {average}")
print(f"Все множества в одном кортеже: {combined_tuple}")

