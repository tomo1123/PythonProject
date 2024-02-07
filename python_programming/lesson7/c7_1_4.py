"""ファイルを作成して書き込む"""
f = open('test.txt', 'w')
f.write('Test\n')
print('I am print', file=f)
f.close()