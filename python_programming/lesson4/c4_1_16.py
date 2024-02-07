"""位置引数とキーワード引数を混ぜて使う"""
def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu('beef', dessert='ice', drink='beer')