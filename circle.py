k = input()
my_count = 0
if '0' in k or '6' in k or '9' in k:
    my_count += 1
if '8' in k:
    my_count += 2

        
print(my_count)