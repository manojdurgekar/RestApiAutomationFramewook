from urllib import response
from pytest import param
import requests
from lib.utilis import build_requests_header
from config import LOG, SESSION



class comments:

    def __init__(self):
        self.comment_url = "/comments"


    #function for GET call

    def get_all_comments(self, app_url, access_token):
        requests_headers = build_requests_header(access_token)
        response = SESSION.get(f"{app_url}{self.comment_url}",headers=requests_headers)
        return response

    # function for POST call 
    def create_comment(self, app_url, access_token, message):
        LOG.info("Create comment ")
        request_headers = build_requests_header(access_token)
        response = SESSION.post(f"{app_url}{self.comment_url}/",headers=requests_headers, params=payload)
        return response

    #Function for PUT call 
    def update_comment(self, app_url, access_token,comment_id, **kwargs):
        LOG.info("Update comment ")
        request_headers = build_requests_header(access_token, content_type="application/json")
        payload = {}

        if "message" in kwargs:
            payload["comment_text"] = kwargs["message"]


        if "likes" in kwargs:
            payload["likes"] = kwargs["likes"]

        LOG.debug(f"Request Payload: {payload}")
        response = SESSION.put(f"{app_url}{self.comment_url}/{comment_id}",headers=request_headers, json=payload)
        return response 

    #Function for deleting a comment using delete call 

    def delete_comments(self, app_url, access_token, comment_id):

        LOG.info("delete_comment ")
        request_headers = build_requests_header(access_token)
        response = SESSION.delete(f"{app_url}{self.comment_url}/{comment_id}",headers=request_headers)

        return response
    


        