# Задача 6
# Найти сумму цифр числа.
#     Пример:
#     254314
#     Сумма цифр числа - 19(2+5+4+3+1+4)

count = 0
for i in '254314':
    count += int(i)

print(count)

