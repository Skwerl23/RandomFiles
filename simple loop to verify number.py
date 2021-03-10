while True:
    age = input("Please enter age: ")
    try:
        age = int(age)
        break
    except:
        print("You entered an invalid value, please try again.")
if age <= 24:
    print("You are Gen-Z")
elif age <= 40: 
    print("You are Gen-Y")
elif age <= 56:
    print("You are Gen-X")
else:
    print("You are a baby boomer")
