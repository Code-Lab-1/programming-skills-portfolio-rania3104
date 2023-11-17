#Exercise 3
glossary={"List":"a data structure used to store multiple values in a single variable",
"Variable":"container to store data values.",
"Loop":"a sequence of instructions repeated continuously until a certain condition is reached.",
"Iteration":"number of times a loop has been executed.",
"String":"a collection of words and characters"}

for word, meaning in glossary.items():
    print("\n"+word+":",meaning)

glossary["Dictionary"]="a data structure used to store key:value pairs."
glossary["Key"]="unique containers that stores values of dictionaries."
glossary["Value"]="any character, number or word stored in the key."
glossary["Data Structure"]="a format used maintaining, storing and organizing data in a structured manner."
glossary["Comments"]="sentences that are not part of the code but increases its readibility."

print("\n"+"Updated glossary:")
for word, meaning in glossary.items():
    print("\n"+word+":",meaning)