"""Напишете програма која ќе прочита број од корисникот и ќе го провери дали тој е парен, и потоа ќе испечати соодветната порака."""

x1 = int(input('Внесете еден број:'))

p_div2 = x1%2

if p_div2 == 0:
    print(f'Бројот {x1} е парен број')
else:
    print(f'Бројот {x1} е непарен број')  
