a = input()
b = input()
c = input()
# lst = [a, b, c]
# lst.sort(key=lambda x: (len(x), x))
if len(a) > len(b) or len(a) == len(b) and a > b:
    a, b = b, a

if len(b) > len(c) or len(b) == len(c) and b > c:
    b, c = c, b

if len(a) > len(b) or len(a) == len(b) and a > b:
    a, b = b, a

print(a)