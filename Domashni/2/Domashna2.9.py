""" Вежба 9: Напиши програма што ќе бара од корисникот да внесе 5 броеви и да ги зачува во листа. Потоа, испечати го збирот на тие броеви."""

lista = []
zbir = 0

for i in range(1,6):
    x = int(input(f'Внесете 5 броеви,{i}: '))
    zbir = zbir + x
    lista.append(x)
    
 
print(f'Вкупниот збир на бреовите во листата {lista} е {zbir}')