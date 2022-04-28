# Задача 10
# Найти количество цифр 5 в числе
# Пример: 543231235643
# 'В числе 2 5-ки.'

number = 543231235643
finding_digit = []
for i in list(str(number)):
    if i == '5':
        finding_digit.append(i)

print('В числе', len(finding_digit), '5-ки')
