"""文字列に含まれるアルファベットを数える"""
s = "fdjsafiewafjdsaeiwfdafke"

d = {}
for c in s:
    d[c] += 1
print(d)