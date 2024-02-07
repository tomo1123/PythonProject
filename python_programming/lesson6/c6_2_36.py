"""__str__"""
class Word(object):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'word!!!!!!'

w = Word('test')
print(w)