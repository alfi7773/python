def word_dict(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0)+1
    return freq

print(word_dict("Hello world hello")) 
