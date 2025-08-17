def longest_word(sentense):
    words = sentense.split()
    return max(words, key=len)

print(longest_word("MyLover"))