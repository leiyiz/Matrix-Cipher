from operator import add

m = [1, 2, 3, 4, 5]
m2 = [6, 7, 8, 9, 10]
m3 = list(map(add, m, m2))
m4 = [a + b for a, b in zip(m, m2)]
print(m3)
print(m4)
m4 = list(map(lambda x: x - 97, m4))
print(m4)