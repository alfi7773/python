# a, b = map(int, input().split())
# c, d = map(int, input().split())

# print(a,':',b)
# print(c,':',d)
# result = a+c, b+d
# print(result)



h,m = map(int,input().split(":")) 
nh,nm = map(int,input().split()) 
n = (h*60 + m +nh*60+nm)%1440 
print("0"+str(n//60) 
if n//60<10 
else n//60,end=":") 
print( "0"+str(n%60) if n%60<10 else n%60)
