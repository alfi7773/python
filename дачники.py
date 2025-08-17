def sq(Ax, Ay, Bx, By, Cx, Cy):
    return abs((Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By)) / 2)

n = int(input())
count = 0

for i in range(n):
    Ox,Oy, Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, input().split())
    s = sq(Ax, Ay, Bx, By, Cx, Cy) + sq(Ax, Ay, Dx, Dy, Cx, Cy)
    s1 = sq(Ax, Ay, Bx, By, Ox, Oy)
    s2 = sq(Cx, Cy, Bx, By, Ox, Oy)
    s3 = sq(Ax, Ay, Dx, Dy, Ox, Oy)
    s4 = sq(Cx, Cy, Dx, Dy, Ox, Oy)
    
    if s == s1 + s2 + s3 + s4:
        count += 1
        
        
print(count)