# question = int(input('Введите число: '))

# if question % 2 == 0:
#     print('Число чётное!')
# else:
#     print('Число нечётное!')



# first = int(input('Введите первое число: '))
# second = int(input('Введите второе число: '))

# print(first+second)





# string = input('Введите строку: ')
# print(len(string))



# name = input('Введите имя: ')
# print(f'Приветствую {name}')



# for i in range(1, 11):
#     print(i)

# user = input('Введите слово: ')

# print(user*2)

# user = input('Введите слово: ')

# a = user[::-1]
# print(a)

# if user == a:
#     print('Это палиндром!')
# else:
#     print('К сожаление нет')



# user = int(input('ваше число: '))

# for i in range(1, user+1):
#     if i % 2 == 0:
#         print(i)



# first = int(input('первое число '))
# second = int(input('второе число '))
# third = int(input('третье число '))
#
# my = max(first, second, third)
# print(f'Самое большое: {my}')











# positive = 0
# negative = 0

# for i in range(10):
#     integer = int(input("Number: "))
#     if integer > 0:
#         positive = 1
#         print("Positive")
#     if integer < 0:
#         negative = 1
#         print("Negative")

# 1
# world = "tРe_stАalth-warrior"
# def upper(text):
#     text = text.replace('-', ' ').replace('_', ' ')
   
#     return text[0].lower() + ''.join(world.capitalize() for world in text[:].split(' '))
#         # text[0]
#     # elif ' ' in text:
#     #     return ''.join(world.capitalize() for world in text.split(' '))
    
# print(upper(world))


# world = "The-stealth_warrior"
# def upper(text):
#     text = text.replace('-', ' ').replace('_', ' ')
#     x=text.split(' ')
   
#     return x[0]+ ''.join(world.capitalize() for world in x[1:])
#         # text[0]
#     # elif ' ' in text:
#     #     return ''.join(world.capitalize() for world in text.split(' '))
    
# print(upper(world))



# 2
# user = input('Имя вашего питомца: ')

# def maskify(user):
#     if len(user) <= 4:
#         return '#' * len(user)
#     else:
#         return '#' * (len(user)-4)+user[-4:]
        
# print(maskify(user))



# 3
# user = input('буква с алфавита: ')

# def position(user):
#     positions = ord(user) - ord('a') + 1
#     print(positions)

# position(user) 


# 4
# user = input('буква с алфавита: ')
# user2 = input('буква с алфавита: ')

# def boolean(val1, val2 ):
#     if val1[-1:] == val2[-1:]:
#         print('true')
#     else:
#         print('false')

# boolean(user, user2)



# 5
# def divisors(num, my_list= None):
#     if my_list == None:
#         my_list = []
        
#     for i in range(1,num+1):
#         if num % i == 0:
#             my_list.append(i)
#     return my_list[1:]

# a = divisors(16)
# print(a)



# 6
# def uniqe(a, b):
#     x = [i for i in a if i not in b]
#     return x

    
# a = [1, 1, 1, 2, 3]
# b = [1, 2, 5]

# find = uniqe(a, b)
# print(find)



# a = [1, 2, 3]
# b = [2]

# find = uniqe

# for i in range(1, n+1):
#     for j in range(1, i):
#         print(j, end='')
#     for j in range(i, n, -1):
#         print(j, end='')
#     print('')








# for i in range(1, n+1):
#     for j in range(1, i):
#         print(j, end='')
#     for j in range(i, n, -1):
#         print(j, end='')
#     print('')



# cube
# n = int(input('введите количество кубков: '))
# sum = 0
# step = 1

# while True:
#     sum += step
#     if n <= sum:
#         print(sum)
#         break

#     step += 1



# 1 3 6 10 15 21


# дома
# 3 = 1 до 8
# 7 = 9 до ...



# alls = g, c, v
# # for i in alls:
# c = v

# print(alls)

# g = 'герань'
# c = 'крокус'
# v = 'фиалка'




# flowers = [g, c, v]

# for i in flowers:
#     new = []
#     if i == flowers[1]:
#         i = v
#         new.append(i)
#     elif i == flowers[0]:
#         i = c
#         new.append(i)
#     else:
#         i = g
#         new.append(i)
#     print(new)




# n = int(input('num: '))

# sum = n * (n+1) / 2
# print(sum)

