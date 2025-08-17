def divisors(num):
    my_num = []
        
    
    for i in range(1, num+1):
        if num % i == 0:
            my_num.append(i)
    return sum(my_num)
    
print(divisors(5))    