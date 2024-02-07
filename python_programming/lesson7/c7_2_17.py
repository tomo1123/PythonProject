"""ファイルをコピー"""
import shutil
import glob

shutil.copy('test_dir/test_dir2/empty.txt', 'test_dir/test_dir2/empty2.txt')
print(glob.glob('test_dir/test_dir2/*'))