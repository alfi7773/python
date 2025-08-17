k=int(input())
A=input().split()[:k]
sum=0
minn=int(A[0])
m=0
maxx=int(A[0])
n=0
z=1
for i in range(k):
    A[i]=int(A[i])
    if A[i]>0:
        sum+=A[i]
    if A[i]>maxx:
        maxx=A[i]
        m=i
    elif A[i]<minn:
        minn=A[i]
        n=i
        
if m>=n:
    for i in range(n+1,m):
        z*=A[i]
elif m<n:
    for i in range(n-1,m,-1):
        z*=A[i]

print(sum,z)