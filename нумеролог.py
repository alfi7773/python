def recur(number, count=0):
    if len(number) == 1:
        print(number, count)
    else:
        s = 0
        for i in number:
            s += int(i)    
        recur(str(s), count+1)
    
s = input()
recur(s)