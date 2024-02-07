"""ディレクトリの中のディレクトリを調べる"""
import os

os.mkdir('test_dir')
os.mkdir('test_dir/test_dir2')
print(os.listdir('test_dir'))