# a, b, c = input().split()

# if '0' in a or '0' in b or '0' in c:
#     print('no')
# else:
#     print(max(a, b, c))
    

# a = int(input())

# b = a // 2
# c = b // 2
# d = b // 2

# print(d, c, b)



# if not 0 in a:
#     print(max(a, b, c))
#     if not 0 in b:
#         print(max(a, b, c))
#         if not 0 in c:
#             print(max(a, b, c))
# else:
#     print('no')


# if a > b:
#     print(a)
# elif b > a:
#     print(b)
# elif b > c:
#     print(b)
# elif b < c:
#     print(c)
# elif a < c:
#     print(c)
# elif c < a:
#     print(a)





a=input().split()[:3]

for i in range(len(a)):
    a[i]=int(a[i])
print(max(a))