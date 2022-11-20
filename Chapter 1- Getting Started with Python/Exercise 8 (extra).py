#Exercise 8 (extra)
str1=str(input())
print("Original word:", str1)
mid = int(len(str1) / 2)
result = str1[mid - 1:mid + 2]
print("Middle three characters:", result)