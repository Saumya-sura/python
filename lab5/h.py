def is_palindrome(word):
    return word == word[::-1]

user_input = input("Enter a word: ")

if is_palindrome(user_input):
    print(user_input, "is a palindrome!")
else:
    print(user_input, "is not a palindrome.")

