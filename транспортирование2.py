n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))
    
for column in range(n-1, -1, -1):
    for row in range(n-1, -1, -1):
        print(row, column, a[row] [column])
        
# print(1+2+3+4+5+6+7+8+9+10)