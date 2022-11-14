#Exercise 1
x = "What topping would you like on your pizza? Type 'quit' if none: "

while True:
    topping = input(x)
    if topping != 'quit':
        print("I'll add" , topping, "to your pizza.")
    else:
        break