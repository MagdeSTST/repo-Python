""" Задача 2: Напиши програма која бара од корисникот да внесе број и креирај функција која испишува дали тој е позитивен, 
негативен или нула."""

def broj(x):
    if x < 0:
        print('Бројот што го внесовте е негаитивен')
    elif x>0:
         print('Бројот што го внесовте е позитивен')
    else:
        print('Внесовте нула')

x= int(input('Внесте еден број:'))
broj(x)