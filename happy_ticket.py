a = int(input())

d6 = a % 10
d5 = a//10%10
d4 = a//100%10
d3 = a//1000%10
d2 = a//10000%10
d1 = a//100000%10

c = d6, d5, d4
e = d3, d2, d1

if sum(c) == sum(e):
    print('YES')
else:
    print('NO')