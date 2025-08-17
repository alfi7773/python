def is_palindrome(world):
    cleaned = world.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print(is_palindrome("А роза упала на лапу Азора"))