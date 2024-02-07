"""位置引数とタプル化と辞書化"""
def menu(food, **kwargs, *args):
    print(food)
    print(args)
    print(kwargs)

menu('banana', 'apple', 'orange', entree='beef', drink='coffee')