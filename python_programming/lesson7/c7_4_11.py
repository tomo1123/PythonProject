"""コマンド実行時のエラー"""
import subprocess

r = subprocess.run('lsa', shell=True)
print(r.returncode)