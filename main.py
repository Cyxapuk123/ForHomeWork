a = int(input('-->'))
b = int(input('-->'))
c = int(input('-->'))
if a > b and a > c and b > c and b < c:
    print(a)
elif a < b:
    print(b)
elif a > c:
    print(a)
elif a < c:
    print(c)
elif b > c:
    print(b)
elif b < c:
    print(c)