#Exercise 8 (extra)
numbers1= [3, 6, 9, 12, 15, 18, 21]
numbers2 = [4, 8, 12, 16, 20, 24, 28]
result = list()

odd_elements = numbers1[1::2]
print("Odd numbers from list 1:")
print(odd_elements)

even_elements = numbers2[0::2]
print("Even numbers from list 2:")
print(even_elements)

print("Final list:")
result.extend(odd_elements)
result.extend(even_elements)
print(result)