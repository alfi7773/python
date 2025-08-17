# N=int(input())

# B=input().split()[:N]

# A=[]

# C=[]

# n=0

# for i in range(N):
#     if 1<=int(B[i])<=31:
#         if int(B[i])%2==1:
#             A.append(int(B[i]))
#         elif int(B[i])%2==0:
#             C.append(int(B[i]))
#         else:
#             n=1
#         break

# print(' '.join(map(str,A)))

# print(' '.join(map(str,C)))

# if len(C)>=len(A) and n==0:
#     print('YES')
# elif len(C)<len(A) and n==0:
#     print('NO')




a = int(input())
b = list(map(int, input().split()))
c = []
d = []

for i in b:
    if i % 2 == 0:
        c.append(i)
    else:
        d.append(i)
        
print(*d)
print(*c)

if len(c) >= len(d):
    print('YES')
else:
    print('NO')