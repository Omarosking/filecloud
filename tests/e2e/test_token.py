import requests
import pytest

def login_and_get_token():
    url = "http://139.144.168.202/admin/adminlogin"
    payload={'adminuser': 'admin', 'adminpassword': 'Ouroburos2305..'}
    files = []
    headers = {
        'Cookie': 'X-XSRF-TOKEN=mdl00svelfghn1ef0doz; X-XSRF-TOKEN-admin=zfjhalquvw1cxrirkltn; tonidocloud-ah=60ee94f272ac0ab78b3ce0143c99556b8e4ebb2c; tonidocloud-as=c52938ff-c7f5-410a-8646-ff36368747ac; tonidocloud-au=admin'
    }
    response = requests.post(url, headers=headers, data=payload, files=files)
    token_admin = response.cookies.get('X-XSRF-TOKEN-admin')
    token_xsrf = response.cookies.get('X-XSRF-TOKEN')
    tonido_ah = response.cookies.get('tonidocloud-ah')
    tonido_as= response.cookies.get('tonidocloud-as')
    tonido_au = response.cookies.get('tonidocloud-au')
    return response.cookies

def test_something_that_needs_token():
    token = login_and_get_token()
    print(token)
    pytest.fail()
    assert True
