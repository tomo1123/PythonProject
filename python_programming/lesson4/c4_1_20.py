"""位置引数とキーワード引数とデフォルト引数を混ぜて使う"""
def menu(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu('chicken', drink='beer')

