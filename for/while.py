i = int(input('Введите первое целое отрицательное или положительное число: '))
b = int(input('Введите второе целое отрицательное или положительное число: '))

while True:
    if i < -1:
        i = i + 1
        print(i)
    elif i == b + 1:
        break
    elif b < -1:
        b = b + 1
        print(b)
    elif b == i + 1:
        break
