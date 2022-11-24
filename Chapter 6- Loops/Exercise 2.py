#Exercise 2
x = "What is your age? Type 'quit' if you are done.\n"

while True:
    age = input(x)
    if age == 'quit':
        break
    if age < 3:
        print("Your ticket is free")
    elif age < 13:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")