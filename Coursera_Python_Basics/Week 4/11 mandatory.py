# Дана последовательность целых чисел, заканчивающаяся числом 0. Выведите эту последовательность в обратном порядке.
# При решении этой задачи нельзя пользоваться массивами и прочими динамическими структурами данных.Рекурсия вам поможет.
def inverse():
    n = int(input())
    if n != 0:
        inverse()
    print(n)


inverse()
