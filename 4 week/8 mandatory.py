# Возводить в степень можно гораздо быстрее, чем за n умножений! Для этого нужно воспользоваться следующими
# рекуррентными соотношениями: aⁿ = (a²)ⁿ/² при четном n, aⁿ=a⋅aⁿ⁻¹ при нечетном n. Реализуйте алгоритм быстрого
# возведения в степень. Если вы все сделаете правильно,то сложность вашего алгоритма будет O(logn).

a = float(input())
n = float(input())


def func(a, n):
    if n == 1:
        print(a)
    elif n % 2 == 0:
        print((a ** 2) ** (n / 2))
    elif n % 2 != 0:
        print(a * (a ** (n - 1)))


func(a, n)