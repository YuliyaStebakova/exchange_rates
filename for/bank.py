# банковская карта. вводим количество денег, потом вводим расходы, пока они не превышают баланс,если превысили, мы должны получить, сколько покупок и сколько осталось денег


#

a = int(input('Баланс на карте: '))
#c = ''
i = 0
while True:
    b = int(input('Расходы: '))
    i = i + 1
    a = a - b
    if a > 0:
        print(f'операция выполнена: {i}, остаток на балансе: {a}')
    elif a <= 0:
        print(f'отказано, количество операций : {i - 1}, остаток на балансе: {a + b}')
        break