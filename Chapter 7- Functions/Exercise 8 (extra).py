#Exercise 8 (extra)
def Percentage():
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
  total=a+b+c+d+e
  average=(total/5)
  percentage=((average/total)*100)
  print("The percentage is=",percentage,"%")

Percentage()