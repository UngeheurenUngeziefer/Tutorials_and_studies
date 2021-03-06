# Улитка ползет по вертикальному шесту высотой H метров,
# поднимаясь за день на A метров, а за ночь спускаясь на B метров.
# На какой день улитка доползет до вершины шеста?
# Программа получает на вход целые H, A, B. Гарантируется, что A > B ≥ 0.
H = int(input())            # длина отрезка
A = int(input())            # дневной шаг
B = int(input())            # ночной шаг назад

step = A - B                # суточный шаг
L = (H - A)                 # длина без последнего шага
print(((L + step - 1) // step) + 1)
# длина без последнего шага + суточный шаг (делается для округления вверх)
# минус шаг на 1 пункт (делается для ситуации с нечётным суточным шагом (подробнее ниже))

# минус шаг на 1 пункт при суточном шаге = 1 даёт просто длину (L(+1-1)) без последнего шага в первой части формулы
# далее мы просто делим эту длину на количество суточных шагов (step) и добавляем последний шаг (+ 1) получая ответ

# минус шаг на 1 пункт при суточном шаге > 1 даёт:
# при чётном суточном шаге минус шаг на 1 пункт можно было бы не делать, например при данных 10 5 1 суточный шаг 4
# 8 или 9 // 4 = разницы нет

# при нечётном суточном шаге минус шаг на 1 пункт необходим, например при данных 10 4 1 суточный шаг 3
# 8 // 3 = 2 а вот 9 // 3 = 3
# потому что к длине без последнего шага (L) добавляется суточный шаг (step), а потом мы делим это
# на сам суточный шаг (step). Без отнятой единицы (-1) сверх нужного результата мы получим ещё один шаг (step) (+1)
# нам же необходимо на данном этапе только округлить вверх
# округление вверх тоже нужно не во всех случаях, но необходимо в некоторых

# (L + step - 1) = здесь получаем длину отрезка без последнего шага округлённую в большую сторону или вверх

# далее производим деление без остатка (// чтобы убрать округление вверх) на суточный шаг
# в результате чего получаем количество дней за которые улитка проходит длину без последнего шага (L)

# добавляем ещё один день (+1) в котором улитка достигает конца отрезка


# второй вариант
X = int(input())
A = int(input())
B = int(input())
dist = 0
days = 0

while True:
    dist += A
    days += 1
    if dist >= X:
        break
    dist -= B
print(days)
