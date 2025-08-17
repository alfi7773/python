def md(a, b):
    while b:
        a, b = b, a % b
    return a
        

a, b = map(int, input().split())

lcm = (a*b) // md(a, b)
print(lcm)



# print(108//36)
# print(108//27)

# print(36*3)
# print(27*4)
