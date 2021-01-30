def is_palindrome(word):
    return word == word[::-1]


word = input()
reversed_word = is_palindrome(word)

if reversed_word:
    print("Yes")
else:
    print("No")
