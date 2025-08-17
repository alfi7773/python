def nums(num):
    new_list = []
    for i in range(1, num):
        if num % i == 0:
            new_list.append(i)
    return max(new_list)

print(nums(6))