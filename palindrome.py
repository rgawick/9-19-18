word = input("Please enter a word: ")

def reverse(x):
    return x[::-1]

def is_palindrome(s):
    rev = reverse(s)
    if (s == rev):
        return True
    return False


answer = is_palindrome(word)

if answer == True:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")
