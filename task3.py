# вывести все целые степени двойки
n = int(input("введите число: "))
i = 0
final = 1
while final < n + 1:
    print(final, end=' ')
    i += 1
    final = 2 ** i