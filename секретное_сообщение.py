n, m = map(int, input().split())

mas = list(map(int,input()))
count = 0

for i in range (len(mas)):
    count += 1
    
if count == 2 == m:
    print('NO')
else:
    print('YES')