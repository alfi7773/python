a = [1, 3, 4, 10, 6, 5]

def func(a, item):
    for i in a:
        if item == i:
            print(i)

print(func(a, 6))