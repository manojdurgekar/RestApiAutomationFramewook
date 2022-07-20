#pytest expects the test to retrieve fixtures from conftest.py file 
import pytest
import requests
from config import SESSION
from config import APP_URL, ADMIN_USER, ADMIN_PASSWORD,LOG


#fixture for login and getting the access token 

@pytest.fixture(scope="session")
def login_as_admin():
    LOG.info("login_as_admin()")
    
    payload ={"username":ADMIN_USER,"password":ADMIN_PASSWORD}
    LOG.debug("login payload : {payload}")
    response = SESSION.post("{APP_URL}/auth/login", data=payload)
    assert response.ok

    access_token = response.json()["access_token"]
    yield access_token

