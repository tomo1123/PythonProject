"""オブジェクトにあとから変数を追加する"""
class T(object):
    pass

t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)