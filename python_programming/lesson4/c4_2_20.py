"""ジェネレーター"""
def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
print(next(g))
print(next(g))
print(next(g))
print(next(g))