""" Вежба 11: Напиши програма што ќе бара од корисникот да внесе реченица.
 Раздели ја реченицата на зборови и зачувај ги во листа. Потоа, испечати го должината на секој збор во листата."""

lista_zbor = []
br = 1
rec = input('Внесете една реченица: ')
lista_zbor = rec.split(" ")
print(lista_zbor)

for i in lista_zbor:
    x = len(i)
    print(f'Должината на {br} збор е {x}')
    br = br + 1
   