a = []

for i in range(4):
    a.append(list(input()))
    
count = 0
for i in range(3):
    for j in range(3):
        if a[i][j] == a[i][j+1] == a[i+1][j] == a[i+1][j+1]:
            count += 1
            
if count > 0:
    print('No')
else:
    print('Yes')