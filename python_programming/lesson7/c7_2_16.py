"""ディレクトリの中のファイルを調べる"""
import pathlib
import glob

pathlib.Path('test_dir/test_dir2/empty.txt').touch()
print(glob.glob('test_dir/test_dir2/*'))