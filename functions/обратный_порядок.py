def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

print(reverse_words("Я люблю Python"))  # "Python люблю Я"
