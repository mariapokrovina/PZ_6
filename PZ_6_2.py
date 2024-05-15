#Дан список A размера N. Сформировать новый список B
# того же размера, элементы которого оперделяются следующим
# образом: BK = 2*АK, если АK Б5    AK/2 в противном случае.
def main():
    a = [[0.0] * 2 for _ in range(10)]
    n = (input("введите N: "))
    while type(n) != int:
        try:
            n = int(n)
        except ValueError:
            print("Неправильно ввели!")
            n = (input("введите N: "))
    for i in range(n):
        print(f"a[{i + 1}]:")
        a[i][0] = float(input("  x : "))
        a[i][1] = float(input("  y : "))

    amax = 0
    rmax = 0.0
    for i in range(n):
        if a[i][0] < 0 and a[i][1] > 0:
            r = math.sqrt(a[i][0] ** 2 + a[i][1] ** 2)
            if r > rmax or i == 0:
                rmax = r
                amax = i

    print(f"A {amax + 1} :")
    print(f" x: {a[amax][0]}")
    print(f" y: {a[amax][1]}")


if __name__ == "__main__":
    main()