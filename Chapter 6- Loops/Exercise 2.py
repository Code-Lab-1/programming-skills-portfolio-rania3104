#Exercise 2
x = "What is your age?\n"

while True:
    age = int(input(x))
    if age < 3:
        print("Your ticket is free")
    elif age < 13:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")