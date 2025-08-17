# a, b = map(int, input().split())
# a -= 1
# b -= 1
# print(a, b)

a = list(map(int,input().split()))
ch_num = []
nch_num = []
for i in a:
    if i % 2 == 0:
        ch_num.append(i)
    else:
        nch_num.append(i)
        
print(max(ch_num) + min(nch_num))