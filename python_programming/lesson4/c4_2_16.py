"""lambdaで簡潔に書く"""
l = ['Mon', 'tue', 'Wed', 'Thu', 'Fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())

