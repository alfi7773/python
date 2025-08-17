def count_vowels(text):
    vowels = "аеёиоуыэюя"
    return sum(1 for char in text.lower() if char in vowels)

print(count_vowels("Привет, как дела?"))  # 5
