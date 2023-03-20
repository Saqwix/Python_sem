# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


N = abs(int(input('Введите число N ')))
S = 0
K = 2
for i in range(N):
    if S != 1:
        K = K ** i
        if K <= N:
            print(K, end=' ')
            K = 2
        else:
            S = 1
    else:
        i = N