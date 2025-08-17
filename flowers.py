flowers = ['G', 'C', 'V']
K = int(input('введите количество дней: '))

K %= 6 
for _ in range(K):
    flowers = [flowers[0], flowers[2], flowers[1]]
    flowers = [flowers[1], flowers[0], flowers[2]]


print(flowers)