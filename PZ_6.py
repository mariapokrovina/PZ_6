#Дан целочисленный список размера N, не содержащий одинаковых чисел
# . Проверить, образуют ли его элементы арифметическую прогрессию. Если
# образуют, то вывести разность прогрессии, если нет - вывести 0.
n = (input("введите N: "))
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = (input("введите N: "))
a = []
for i in range(n):
    a.append(int(input("введите a[{}] : ".format(i+1))))

r = a[1] - a[0]
for i in range(1, n):
    if r != a[i] - a[i-1]:
        r = 0

print(r)