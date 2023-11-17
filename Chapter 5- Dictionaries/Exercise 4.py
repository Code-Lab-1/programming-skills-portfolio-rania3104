#Exercise 4
rivers = {"Amazon":"Brazil","Nile":"Egypt","Mississippi":"United States"}

for river, country in rivers.items():
    print("The",river, "runs through", country + ".")

print("\nThe rivers named in this dictioary are:")
for river in rivers.keys():
    print("- " + river)

print("\nThe countries named in this dictionary are:")
for country in rivers.values():
    print("- " + country)