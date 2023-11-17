#Exercise 9 (extra)
marks=int(input())
if marks > 80 and marks < 90 or marks == 90:
  print("A+")
elif marks > 70 and marks < 80 or marks == 80:
  print("A")
elif marks > 60 and marks < 70 or marks == 70:
  print("B")
elif marks > 40 or marks == 40:
  print("Pass")
else:
  print("Fail")