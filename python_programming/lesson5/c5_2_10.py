"""defaultdict"""
s = "fdjsafiewafjdsaeiwfdafke"

from collections import defaultdict
d = defaultdict(int)
for c in s:
    d[c] += 1
print(d)