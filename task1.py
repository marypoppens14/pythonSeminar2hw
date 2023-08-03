# Выведите минимальное количество монет, которые нужно перевернуть.
n = int(input("Введите число монет: "))
k = 0
for i in range(n):
    x = int(input())
    if x == 1:
        k += 1
if k < n/2:
    print(k)
else:
    print(n - k)