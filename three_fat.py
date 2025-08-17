# a, b, c = map(int, input().split())
# print(max(a**1, b*2, c*3))


M1, M2, M3 = map(int, input().split())
if 94 <= M1 <= 727 and 94 <= M2 <= 727 and 94 <= M3 <= 727:
    print(max(M1, M2, M3))
else:
    print('Error')
