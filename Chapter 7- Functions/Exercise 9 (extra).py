#Exercise 9 (extra)
def maximum():
    print("Enter the first number: ")
    a=int(input()) or float(input())
    print("Enter the second number: ")
    b=int(input()) or float(input())
    print("Enter the third number: ")
    c=int(input()) or float(input())

    print("The biggest number is: ")
    if a>b and a>c:
      print(a)
    elif b>a and b>c:
      print(b)
    else:
      print(c)

maximum()