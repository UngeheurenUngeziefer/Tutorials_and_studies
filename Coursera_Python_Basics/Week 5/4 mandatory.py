# По данному натуральному n≤9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.

n = int(input())    # 0-9

nums = 1, 2, 3, 4, 5, 6, 7, 8, 9

for i in range(1, n + 1):
    print(*(nums[0:i]), sep='')
