sentence = str(input ("Enter a sentence: "))
dictionary = dict ({})
for x in sentence:
    dictionary [x] = sentence.count(x)

print (dictionary)