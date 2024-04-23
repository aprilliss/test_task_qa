import requests


user_data = {
        "user": {
            "login": "inna4",
            "email": "pintatest5@gmail.com",
            "password": "awdasd"
        }
    }
new_data = {
        "user": {
            "login": "inna7",
            "email": "pintatester77@gmail.com",
            "password": "awdasd"
        }
    }
TOKEN = ''


def create_user():
    url = 'https://favqs.com/api/users'

    headers = {
        'Authorization': 'Token token="bf4ee66e88953394bd1d89a9b309f0f7"',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=user_data, headers=headers)
    return response


def create_user_session(json):
    url = 'https://favqs.com/api/session'
    headers = {
        'Authorization': 'Token token="bf4ee66e88953394bd1d89a9b309f0f7"',
        'Content-Type': 'application/json',
    }

    session = requests.post(url, json=json, headers=headers)
    return session


def test_create_user():
    global TOKEN
    response = create_user()
    assert response.status_code == 200
    json = {
        "user": {
            "login": user_data['user']['login'],
            "password": user_data['user']['password']
        }
    }
    response2 = create_user_session(json)
    assert response2.json().get('login') == user_data['user']['login']
    assert response2.json().get('email') == user_data['user']['email']
    TOKEN = response2.json().get("User-Token")


def test_update_user():
    url = f'https://favqs.com/api/users/{user_data['user']['login']}'
    headers = {
        'Authorization': 'Token token="bf4ee66e88953394bd1d89a9b309f0f7"',
        'Content-Type': 'application/json',
        'User-Token': TOKEN
    }
    json = {
        "user": {
            "login": new_data['user']['login'],
            "password": new_data['user']['password']
        }
    }
    response = requests.put(url, json=new_data, headers=headers)
    assert response.status_code == 200
    session = create_user_session(json)
    assert session.json().get('login') == new_data['user']['login']
    assert session.json().get('email') == new_data['user']['email']


if __name__ == '__main__':
    test_create_user()
    test_update_user()


