import requests
import pytest
import yaml


with open('logpass.yaml') as f:
    data = yaml.safe_load(f)


name = data['user']
passwd = data['password']
title = data['title']
description = data['description']
content = data['content']


@pytest.fixture()
def login():
    r = requests.post('https://test-stand.gb.ru/gateway/login', data={'username': name, 'password': passwd})
    return r.json()['token']


@pytest.fixture()
def create_post():
    p = requests.post('https://test-stand.gb.ru/gateway/posts', data={'title': title, 'description': description,
                                                                      'content': content})
    return p.json()['token']


@pytest.fixture()
def text1():
    return 'The text of the new post sem3'


@pytest.fixture()
def text2():
    return 'Post 1 description'