from email import message
import pytest
import requests
from lib.comments import comments
from lib.utilis import build_request_headers
from config import APP_URL,LOG
import logging


def test_get_all_comments(login_as_admin):
      
   #Hit get comments endpoint 
    LOG.info("test_get_all_comments")
    response = comments().get_all_comments("http://localhost:8080", login_as_admin)
    logging.info("Log this ")
    LOG.debug(response.json())
    assert response.ok

# Test scenario to demonstarte end to end flow by performing create comment, update comments and then delete comments 
def test_CreateUpdateDelete(login_as_admin):
   LOG.info("test_CreateUpdateDelete")

   # calling the create comment function to do a POST call for create comment
   
   response = comments().create_comment(APP_URL, login_as_admin, "First post call")
   assert response.ok
   response_data= response.json()
   comment_id = response_data["id"]
   LOG.debug(response_data)
   assert response_data["comment_text"] == "First post call"
   response = comments().update_comment(APP_URL, login_as_admin, comment_id,message="Updated to second POST",likes =3)

   assert response.ok
   response_data = response.json()
   LOG.debug(response_data)

   assert response.ok

   response_data = response.json()
   LOG.debug(response_data)
   assert response_data["comment_text"] == "Updated to second POST"

   assert response_data["likes"] == 3

   response = comments().delete_comment(APP_URL, login_as_admin, comment_id)
   assert response.ok
   response_data = response.json()
   LOG.debug(response_data)
   assert response_data["detail"] == f"Deleted comment{comment_id}"

