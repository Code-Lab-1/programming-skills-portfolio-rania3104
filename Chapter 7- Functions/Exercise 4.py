#Exercise 4
def make_shirt(size='large', msg='I love Python!'):
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, \"' + msg + '\"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Gotta be fast!')