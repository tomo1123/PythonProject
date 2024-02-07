"""円の面積を求める - 2とおりの計算を実行する"""
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.14159)

print(ca1(10))
print(ca2(10))
