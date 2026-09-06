'''
Алгоритм вычисления значения функции F(n), где n - целое число, задан следующими соотношениями:

F(n) = n при n < 10
F(n) = 3n + F(n - 3), если n >= 10

Чему равно значение выражения (F(6250) + 2 * F(6244)) / F(6238)?

В ответе запишите целую часть полученного числа.
'''

from sys import *

setrecursionlimit(10**6)


def F (n):
  if n < 10:
    return n
  else:
    return 3*n + F (n -3)
print ((F(6250)+2*F(6244))/F(6238))



#     return 3*n + F (n -3)
#   [Previous line repeated 995 more times]
#   File "/Users/mvgordeev/Documents/GitHub/Alina/main.py", line 14, in F
#     if n < 10:
# RecursionError: maximum recursion depth exceeded in comparison