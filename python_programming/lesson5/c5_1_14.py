"""try-except文を使ったモジュールの読み込み"""
try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils