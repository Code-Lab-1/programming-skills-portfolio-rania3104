#Exercise 6 (extra)
print("Printing current and previous number and their sum in a range(10)")
previousnum = 0

for i in range(1, 11):
    sum = previousnum + i
    print("\nCurrent Number", i, "\nPrevious Number ", previousnum, "\nSum: ", sum)
    previousnum = i