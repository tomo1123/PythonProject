"""finally"""
l = [1, 2, 3]
i = 5
try:
    l[i]
finally:
    print("clean up")