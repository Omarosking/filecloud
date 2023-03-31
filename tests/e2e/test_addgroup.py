import pytest
import requests
import xml.etree.ElementTree as ET
import httpx

# Data test
url = "http://139.144.168.202/admin/"

# Tokens should generated and reclaced
headers_dict_admin = {
  'Cookie': 'X-XSRF-TOKEN=mdl00svelfghn1ef0doz; X-XSRF-TOKEN-admin=igpcdulbvjtkq1rvswvv; X-XSRF-TOKEN-user=zyqlc1ymzvbchnrczelx; tonido-login-hash=1cc3310543b7065eb884be8a221138ca68497e1d; tonido-login-seed=45126e52-30d5-43b0-8d8a-98c09bce58aa; tonido-login-user=testuser; tonido-share-login-hash=; tonido-share-login-seed=; tonido-share-login-user=; tonidocloud-ah=fcc44ddb9f016c13a501b67279f6a816dc66bcf6; tonidocloud-as=416c9cc4-92cc-44e3-9228-09450268be1f; tonidocloud-au=admin'
}
# Tokens should generated and reclaced
headers_dict_user = {
    'Cookie': 'X-XSRF-TOKEN=mdl00svelfghn1ef0doz; X-XSRF-TOKEN-admin=qhwmvr1ezyzokkceftha; X-XSRF-TOKEN-user=zyqlc1ymzvbchnrczelx; tonido-login-hash=1cc3310543b7065eb884be8a221138ca68497e1d; tonido-login-seed=45126e52-30d5-43b0-8d8a-98c09bce58aa; tonido-login-user=testuser; tonido-share-login-hash=; tonido-share-login-seed=; tonido-share-login-user=; tonidocloud-ah=3407b1ada397bba7c008130df884afda35eb2ac2; tonidocloud-as=282817c3-6d14-46e0-bc2e-e61fafacccfb; tonidocloud-au=admin'
}


def login_and_get_token():
    payload = {'adminuser': 'admin', 'adminpassword': '123456789A.'}
    files = []

    response = requests.post(url + 'adminlogin', headers=headers_dict_admin, data=payload, files=files)
    cookies = response.cookies
    cookie_dict = requests.utils.dict_from_cookiejar(cookies)
    print(cookie_dict)
    return cookie_dict


# create groups
@pytest.mark.parametrize("groupname", ['Accounting', 'Operations', 'Engineering', 'Consultants'])
def test_create_groups(groupname):
    payload = {'groupname': groupname}
    files = []

    headers = login_and_get_token()

    response = requests.request("POST", url + 'addgroup', headers=headers_dict_admin, data=payload, files=files)
    assert response.status_code == 200
    print(headers)


# create users

@pytest.mark.parametrize("username, displayname, email, password, authtype, status", [
    ("user1", "displayname1", "email1@sds.com", "password1", "0", "1"),
    ("user2", "displayname2", "email2@sds.com", "password2", "0", "1"),
    ("user3", "displayname3", "email3@sds.com", "password3", "0", "1"),
    ("user4", "displayname4", "email4@sds.com", "password4", "0", "1"),
    ("user5", "displayname5", "email5@sds.com", "password4", "0", "1"),
    ("user6", "displayname6", "email6@sds.com", "password4", "0", "1"),
    ("user7", "displayname7", "email7@sds.com", "password4", "0", "1"),
    ("user8", "displayname8", "email8@sds.com", "password4", "0", "1"),
    ("user9", "displayname9", "email9@sds.com", "password4", "0", "1"),
    ("user10", "displayname10", "email10@sds.com", "password4", "0", "1"),
    ("user11", "displayname11", "email11@sds.com", "password4", "0", "1"),
    ("user12", "displayname12", "email12@sds.com", "password4", "0", "1"),
    ("user13", "displayname13", "email13@sds.com", "password4", "0", "1"),
    ("user14", "displayname14", "email14@sds.com", "password4", "0", "1"),
    ("user15", "displayname15", "email15@sds.com", "password4", "0", "1"),
])
def test_add_user(username, displayname, email, password, authtype, status):
    files = []

    payload = {
        'username': username,
        'displayname': displayname,
        'email': email,
        'password': password,
        'authtype': authtype,
        'status': status
    }

    response = requests.post(url + 'adduser', headers=headers_dict_admin, data=payload, files=files)
    assert response.status_code == 200


# Add user to group
def test_get_group_list():
    payload = {'': ''}
    files = []
    response = requests.request("GET", url, headers=headers_dict_admin, data=payload, files=files)
    root = ET.fromstring(response.text)
    group = root.find('group')
    groupid = group.find('groupid').text
    print(response.text)
    print(groupid)
    pytest.fail()


# Delete users
def test_delete_user():
    for i in range(1, 16):
        payload = {'profile': 'user{}'.format(i)}
        response = requests.post(url + 'deleteuser', headers=headers_dict_admin, data=payload)
    print('User{} deleted'.format(i))


# Upload .docx file for a user

def test_upload_docx_file():
    payload = {'path': '/Users/omarosking/Documents/GitHub/Finally/tests/e2e/test_data.docx'}
    files = []

    response = requests.request("POST", url, headers=headers_dict_user, data=payload, files=files)
    print(response.text)
    pytest.fail()
