#Exercise 4
sandwich_orders = ['chicken', 'boiled egg', 'cheese', 'nutella']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")