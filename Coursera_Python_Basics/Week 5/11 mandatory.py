# Напишите программу, которая находит в массиве элемент, самый близкий по величине к данному числу.
# В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива.
# Во второй строке содержатся N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).
# В третьей строке вводится одно целое число x, не превосходящее по модулю 1000.

z = int(input())
a = [int(i) for i in input().split()]
b = int(input())
lst = []

for i in a:
    r = b - i
    if r == 0:
        print(i)
        exit()
    elif r < 0:
        lst.append(-r)
    elif r > 0:
        lst.append(r)

s = lst.index(min(lst))
print(a[s])
