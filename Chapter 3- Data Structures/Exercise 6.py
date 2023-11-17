#Exercise 6
guests = ["Burak Deniz", "Alex Hales", "Charlie Chaplin","Shawn Mendes"]
print("Hello",guests[0]+"! I would like to invite you to a dinner.")
print("Hello",guests[1]+"! I would like to invite you to a dinner.")
print("Hello",guests[2]+"! I would like to invite you to a dinner.")
print("Hello",guests[3]+"! I would like to invite you to a dinner.")

print("\nSorry",guests[2],"can't make it.")
guests[2]="Engin Akyurek"

print("\nHello",guests[0]+"! I would like to invite you to a dinner.")
print("Hello",guests[1]+"! I would like to invite you to a dinner.")
print("Hello",guests[2]+"! I would like to invite you to a dinner.")
print("Hello",guests[3]+"! I would like to invite you to a dinner.")

print("\nSorry, we can only invite two people to dinner.")

print("\nSorry", guests.pop() + ", there's no room for more than 2 at the table.")
print("Sorry", guests.pop() + ", there's no room for more than 2 at the table.")

print("\nHello",guests[0]+"! I would like to invite you to a dinner.")
print("Hello",guests[1]+"! I would like to invite you to a dinner.")

del(guests[0])
del(guests[0])

print("\n",guests)
