import re

def valid_email(email):
    email_pattern = "^[a-z]+[\._]?[a-z 0-9]+[@gmail.com]+[@cognifyz.com]\w+[.]\w{2,3}$"
  
    search = re.search(email_pattern, email)

    
    if (search):
        print(f"{email} is a valid Email.")

    else:
        print(f"{email} is not a valid Email. Please write a Correct Email!")

while True:
    email_to_check = input("Enter Your Email: ")

    valid_email(email_to_check)



       