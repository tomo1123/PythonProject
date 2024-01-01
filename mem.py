import sqlite3
import time

import memcache

db = memcache. Client(['127.0.0.1:11211'])

conn = sqlite3.connect('test_sqlite2.db')
cors = conn.cursor()
cors.execute(
    'CREATE TABLE IF NOT EXISTS persons('
    'employ_id INTEGER PRIMARY KEY AUTOINCREMENT , name STRING)')
cors.execute('INSERT INTO persons(name) values("Mike")')
conn.commit()


def get_employ_id(name):
    employ_id = db.get(name)
    if employ_id:
      return employ_id
    cors.execute(
      'SELECT * FROM persons WHERE name = ?', (name,)
    )
    person = cors.fetchone()
    if not person:
      raise Exception('No employ')
    employ_id, name = person
    db.set(name, employ_id, time=60)
    return employ_id
  
print(get_employ_id("Mike"))

conn.close()