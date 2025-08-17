n = int(input())
price = list(map(int, input().split()))

i = 0
s = 0
while i < len(price):
    maxs = price[i]
    for j in range(i+1, len(price)):
        if price[j] > maxs:
            maxs = price[j]
    s += maxs
    i+=1
    
print(s)