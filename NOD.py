# def divisors(num, my_list= None):
#     if my_list == None:
#         my_list = []
        
#     for i in range(1,num+1):
#         if num % i == 0:
#             my_list.append(i)
#     return my_list[1:]

# a = divisors(16)
# print(a)


a, b = map(int, input().split())
result = a and b % a
print(result)