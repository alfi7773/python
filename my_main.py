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











positive = 0
negative = 0

for i in range(10):
    integer = int(input("Number: "))
    if integer > 0:
        positive = 1
        print("Positive")
    if integer < 0:
        negative = 1
        print("Negative")
