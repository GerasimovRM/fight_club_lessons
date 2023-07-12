a = int(input())  # 3  3
b = int(input())  # 9  3
c = int(input())  # 9  5
if a > b:
    a, b = b, a

if b > c:
    c, b = b, c

if a > b:
    a, b = b, a

if a ** 2 + b ** 2 == c ** 2:
    ...
elif a ** 2 + b ** 2 < c ** 2:  # тупой
    ...
else:
    ...
