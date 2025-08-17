K, N = map(int, input("введите кол-во ступенек : ").split())

find = [0] * (N + 1)
find[0] = 1  

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if i - j >= 0:
            find[i] += find[i - j]

print(find[N])