"""文字列に含まれるアルファベットを数える"""
s = "fdjsafiewafjdsaeiwfdafke"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)