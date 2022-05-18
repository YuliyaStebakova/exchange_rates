# Вводятся три целых числа. сравнение и результат
a = int(input('Введите первое целое число:'))
b = int(input('Введите второе целое число:'))
c = int(input('Введите второе целое число:'))

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)