import requests

"""POSTでアクセス"""
r = requests.post(
    'http://127.0.0.1:5000/post', data={'username': 'mike'})
print(r.text)

"""PUTでアクセス"""
# r = requests.put(
#     'http://127.0.0.1:5000/post', data={'username': 'mike'})
# print(r.text)

"""DELETEでアクセス"""
# r = requests.delete(
#     'http://127.0.0.1:5000/post', data={'username': 'mike'})
# print(r.text)

"""GETでアクセス"""
# r = requests.get(
#     'http://127.0.0.1:5000/post', data={'username': 'mike'})
# print(r.text)

"""さまざまなメソッドで呼び出し"""
# r = requests.get('http://127.0.0.1:5000/employee/jun')
# print(r.text)
# r = requests.post('http://127.0.0.1:5000/employee', data={'name': 'jun'})
# print(r.text)
# r = requests.put('http://127.0.0.1:5000/employee', data={'name': 'jun', 'new_name': 'sakai'})
# print(r.text)
# r = requests.delete('http://127.0.0.1:5000/employee', data={'name': 'sakai'})
# print(r.text)