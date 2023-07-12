# str, int, float
a = '123'
b = 213
c = 3.5
print(type(a), type(b), type(c))

# str
a = '123'
b = "abc"
print(a + b, b + a)
print(a * 10)

# int float
a = 9
b = 4
print(a + b, a - b, a * b, a ** b, a + b ** 2 / 3)
print(a / b)
print(a // b)
print(a % b)

# преобозование типов
st = '123'
n = int(st)
print(n + 1)

n = 123
st = str(n)

j = 7.7
print(round(j))

k = input()  # str!
