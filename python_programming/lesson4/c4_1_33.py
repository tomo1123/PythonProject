"""キーワード引数の辞書化"""
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice',
}
menu(**d)
