def count_vowels(boom):
    vowels = "аеёиоуыэюя"
    return sum(1 for char in boom.lower() if char in vowels)

print(count_vowels("Привет, как дела?"))  # 5
