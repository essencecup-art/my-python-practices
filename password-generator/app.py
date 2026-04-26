import string
import random
all_in_one = string.ascii_letters
include_number=input("include number(yes/no): ")
include_symbol=input("include symbols(yes/no): ")
if include_number.lower() == "yes":
    all_in_one += string.digits
elif include_number.lower() == "no":
    pass
else:
    print("type yes or no only")
if include_symbol.lower() == "yes":
    all_in_one += string.punctuation
elif include_symbol.lower() == "no":
    pass
else:
    print("type yes or no only")
try:
    password_lenght = int(input("pick your password lenght:"))
except (ValueError, NameError):
    print('please enter a valid number,defaulting length to 8')
    pass_word = 8
pass_word = 0
password = ""
while pass_word < password_lenght:
    password += random.choice(all_in_one)
    pass_word += 1
print(f"your password is: {password}")
