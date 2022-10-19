import requests
from requests import Response
from voluptuous import Schema, PREVENT_EXTRA, Optional
from pytest_voluptuous import S

#Get single user
get_single_user_schema = Schema(
    {
        "data": {
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            "avatar": str
        },
        "support": {
            "url": str,
            "text": str
        }
    },
    required=True,
    extra=PREVENT_EXTRA
)

def test_get_users():
    result: Response = requests.get(
        "https://reqres.in/api/users",
        params={"id": 2}
    )

    assert result.status_code == 200
    assert result.json()['data']['id'] == 2
    assert result.json()['data']['email'] == 'janet.weaver@reqres.in'
    assert result.json()['data']['first_name'] == 'Janet'
    assert result.json()['data']['last_name'] == 'Weaver'
    assert result.json()['data']['avatar'] == 'https://reqres.in/img/faces/2-image.jpg'
    assert result.json() == S(get_single_user_schema)


#Post_create_user
post_create_user_schema = Schema(
        {
            "name": str,
            "job": str,
            "id": str,
            "createdAt": str
        },
        required=True,
        extra=PREVENT_EXTRA
    )

def test_create_user():
    name = 'TestUser'
    job = 'TestJob'

    result = requests.post(
        url="https://reqres.in/api/users",
        json={"name": name, "job": job}
    )

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)
    assert isinstance(result.json()['createdAt'], str)
    assert result.json() == S(post_create_user_schema)

#Put_update_user
put_update_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

def test_update_user():
    name = 'UpdatedUser'
    job = 'UpdatedJob'

    result = requests.put(
        url="https://reqres.in/api/users/2",
        json = {"name": name, "job": job}
    )

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(put_update_user_schema)


#Delete_user
def test_delete_user():
    result = requests.delete('https://reqres.in/api/users/2')
    assert result.status_code == 204

#Post_login_user
post_login_user_schema = Schema(
    {
        "token": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

def test_login_user():
    email = 'eve.holt@reqres.in'
    password = 'cityslicka'

    result = requests.post(
        url="https://reqres.in/api/login",
        json = {"email": email, "password": password}
    )

    assert result.status_code == 200
    assert result.json()['token'] == "QpwL5tke4Pnpja7X4"
    assert result.json() == S(post_login_user_schema)