b, a = input()
c = 'ABCDEFGH'
v = c.index(b) + 1
a = int(a)
if a % 2 == v % 2:
    print('BLACK')
else:
    print('WHITE')
    

