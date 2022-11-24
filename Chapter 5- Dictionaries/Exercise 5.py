#Exercise 5
pet1 = {"Name": "Leah","Species":"Cat","Owner": "Rania"}
pet2 = {"Name": "Maggie","Species":"Parrot","Owner": "Maria"}
pet3 = {"Name": "Cookie","Species":"Dog","Owner": "Penny"}
pet4 = {"Name": "Harry","Species":"Turtle","Owner": "Sara"}
pet5 = {"Name": "Goldie","Species":"Fish","Owner": "Emma"}

pets = [pet1,pet2,pet3,pet4,pet5]

for pet in pets:
    print("\nInformation of", pet['Name']+ ":")
    for key, value in pet.items():
        print("\t" + key + ":", value)