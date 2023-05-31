import requests


def get(token):
    g = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})
    listcont = [i['content'] for i in g.json()['data']]
    return listcont


def test_3(create_post, text2):
    assert text2 in get(create_post)
