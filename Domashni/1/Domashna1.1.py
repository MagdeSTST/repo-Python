"""Напишете програма која ќе прочита два броја од корисникот и ќе го испечати збирот, разликата, производот и количникот на двата броја.
 Споредете кој резултат е поголем, збирот или производот"""

x1 = int(input('Внесете го првиот број:'))
x2 = int(input('Внесете го вториот број:'))

p_sumа = x1 + x2
p_razlika = x1 -x2
p_mnozenje = x1 * x2
p_delenje = x1 / x2

print(f'За двата внесени броеви {x1} и {x2} ги добиваме следните резултати: \n  Сума: {p_sumа} \n  Разлика: {p_razlika} \n  Производ: {p_mnozenje} \n  Количник: {p_delenje}')

if p_sumа > p_mnozenje:
    print('Сумата е поголема')
else:
    print('Производот е поголем')   