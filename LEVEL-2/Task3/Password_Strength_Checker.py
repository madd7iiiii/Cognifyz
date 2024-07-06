import re
from tokenize import Special
from unicodedata import digit

def evaluate_password_strength(password):
    min_length = 8

    lowercase = re.search(r'[a-z]', password)
    uppercase = re.search(r'[A-Z]',password)
    digit = re.search(r'\d', password)
    Special_char = re.search('r[!@#$%^&*(),.?":{}|<>]', password)

    if len(password) < min_length:
        print(f"Weak: Password should be at least {min_length} charecters long.")
    
    elif not uppercase and not digit:
        print("Password must contain at least one uppercase letter, one digit and one special Character.")

    elif not uppercase and not Special_char and digit:
        print("Password must contain at least one uppercase letter and one special character.")

    elif not lowercase and not Special_char and uppercase:
        print("Password must contain at least one lowercase letter, one special Character and one digit.")

    elif not digit:
        print("Password must contain at least one Digit.")

    else:
        print("Password is Strong")
    

while True:
    user_password = input("Enter your password: ")
    evaluate_password_strength(user_password)
    