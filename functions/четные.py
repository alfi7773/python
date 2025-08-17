def filter_even(numbers):
    return [num for num in numbers if num % 2 == 0]

print(filter_even([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
