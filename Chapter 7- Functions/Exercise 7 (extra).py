#Exercise 7 (extra)
def Average():
  print("Enter the first number: ")
  a=int(input()) or float(input())
  print("Enter the second number: ")
  b=int(input()) or float(input())
  print("Enter the third number: ")
  c=int(input()) or float(input())
  print("Enter the fourth number: ")
  d=int(input()) or float(input())
  print("Enter the fifth number: ")
  e=int(input()) or float(input())

  average=((a+b+c+d+e)/5)
  print("The average is =",average)

Average()