'''Для какого наибольшего целого числа А формула

((x ≤ 9) →(x ⋅ x ≤ A)) ⋀ ((y ⋅ y ≤ A) → (y ≤ 9))

тождественно истинна, то есть принимает значение 1 при любых целых неотрицательных x и y?'''


for a in range(1, 10):
  m = []
  for x in (1, 100):
    f = (x / (2*x) < a)   # f = 
    m.append(f)           # m = [True, True, True, True, True, False, True, True, False]
  if m.count(False) == 0:
    print(a)


1
