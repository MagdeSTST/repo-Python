""" Вежба 13: Напиши програма што ќе бара од корисникот да внесе серија на броеви. 
Зачувај ги броевите во листа и потоа испечати ја средната вредност на броевите."""


lista = []
x= int(input('Внесте број колку сакате да биде долга вашата листа: '))
cnt = 1

for i in range(x):
    y = int(input(f'Внесете те го {cnt} број : '))
    lista.append(y)
    cnt = cnt + 1 

z = int ( sum(lista) / x)
print(lista)
print(f'Средната вредноста на листат е {z}')