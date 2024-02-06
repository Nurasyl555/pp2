def palindrome(word):
    if word == word[::-1]:
        return True
    return False
words = input()
print(palindrome(words))