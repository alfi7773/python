a = int(input())
numbers = list(map(int, input().split()))

c, d = [], []
for i in numbers:
    if i % 2 == 0:
        c.append(i)
    elif i % 2 != 0:
        d.append(i)


if len(c) >= len(d):
    print(c)
    print('YES')
elif len(c) <= len(d):
    print(d)
    print('NO')
        