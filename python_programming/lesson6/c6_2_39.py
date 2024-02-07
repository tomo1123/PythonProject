"""オブジェクトの比較"""
class Word(object):
    def __init__(self, text):
        self.text = text

w = Word('test')
w2 = Word('test')
print(w == w2)
print(id(w))
print(id(w2))