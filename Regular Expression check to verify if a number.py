import re
age = input("Please enter age: ")
while not re.match(r'^[0-9]{1,3}$',age):
    print("You entered an invalid value, please try again.")
    age = input("Please enter age: ")
age = int(age)
if age <= 24:
    print("You are Gen-Z")
elif age <= 40: 
    print("You are Gen-Y")
elif age <= 56:
    print("You are Gen-X")
else:
    print("You are a baby boomer")
    
