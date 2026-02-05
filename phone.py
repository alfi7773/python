# a, b, c, t = map(int, input().split())

# if t>a: 
#     print(a*b+(t-a)*c) 
# if t==a: 
#     print(a*b)

# a, b, c = map(int, input().split())
# print(a + b + c)


# a, b = map(int, input().split())
# print(a+b)

a = int(input())
num = 0

for i in range(min(1, a), max(1,a)+1):
    num += i
    
print(num)