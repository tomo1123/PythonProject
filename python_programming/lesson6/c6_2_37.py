"""__len__"""
class Word(object):
    def __init__(self, text):
        self.text = text

    def __len__(self):
        return len(self.text)

w = Word('test')
print(len(w))