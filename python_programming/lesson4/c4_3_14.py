"""if文を使ったジェネレーター内包表記"""
g = (i for i in range(10) if i % 2 == 0)
for x in g:
    print(x)