def is_palindrome(s):
    a = s.replace(" ", "").lower()
    
    return a == s[::-1]

while True:
    word = input("Enter the word: ")
    if is_palindrome(word):
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome.")