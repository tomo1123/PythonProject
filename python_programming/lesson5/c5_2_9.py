"""setdefault"""
s = "fdjsafiewafjdsaeiwfdafke"

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)