from urllib import response
from lib.users import Users
from lib.auth import Auth
from config import APP_URL, LOG, ADMIN_PASSWORD, ADMIN_USER


def test_user_permissions(login_as_admin):
    LOG.info("test_user_permission")

    #create new user and assign "user" role

    new_username = "testadmin"
    new_password = "Kashya123!"
    new_user_roles = "user"
    response = Users().create_user(APP_URL, login_as_admin, new_username, new_password)

    assert response.ok
    response_data = response.json()
    new_user_id = response_data["id"]
    assert response_data["username"] == new_username
    assert response_data["roles"] == "user"

    #Login as the newly created use 

    response = Auth().login(APP_URL, new_username, new_password)
    assert response.ok
    response_data = response.json()
    access_token = response_data["access_token"]

    #check the new user can gethis own info 

    response = Users().get_current_user(APP_URL, access_token)
    assert response.ok
    assert response.json()["username"] == new_username
    assert response.json()["roles"] == new_user_roles

    #check that newly created user can not create other users because user role doesnt have admin privileges

    response = Users().create_user(APP_URL, access_token, "manoj","Notadmn123")
    assert not response.ok

    #check that newly created user can not delete other users as he doesn't admin priveleges 

    response = Users().delete_user(APP_URL, access_token, new_user_id)

    assert not response.ok

    # Finally delete the newly created user but tihs time use admin account 

    response = Users().delete_user(APP_URL, login_as_admin, new_user_id)
    assert response.ok
    

