#Exercise 5
def describe_city(city, country='scotland'):
    msg = city.title() +" is in "+ country.title()+ "."
    print(msg)

describe_city('edinburgh')
describe_city('reykjavik', 'iceland')
describe_city('glasgow')