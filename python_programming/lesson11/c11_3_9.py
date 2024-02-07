"""データベースを利用する関数の準備"""
import sqlite3
from flask import Flask
from flask import render_template
from flask import g
from flask import request

app = Flask(__name__)

"""データベースに接続する処理"""
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('test_sqlite.db')
    return db

"""データベースへの接続を閉じる処理"""
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/employee', methods=['POST', 'PUT', 'DELETE'])
@app.route('/employee/<name>', methods=['GET'])
def employee(name=None):

    if request.method == 'GET':
        return name

@app.route('/')
def hello_world():
    return 'top'

@app.route('/hello')
@app.route('/hello/<username>')
def hello_world2(username=None):
    return render_template('hello.html', username=username)

@app.route('/post', methods=['POST', 'PUT', 'DELETE'])
def show_post():
    return str(request.values['username'])

def main():
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()