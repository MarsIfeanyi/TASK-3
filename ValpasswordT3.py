#Program to check the validity of password input by the user
import re
a = input("Please enter your password >>:")
b = True
while b: 
    if (len(a)<6 or len(a)>12):
        break
    elif not re.search("[a-z]",a):
        break
    elif not re.search("[0-9]",a):
        break
    elif not re.search("[A-Z]",a):
        break
    elif not re.search("[$#@]",a):
        break
    elif re.search("\s",a):
        break
    else:
        print("valid password")
        b = False
        break
if b:
    print("Invalid Password, Try again")