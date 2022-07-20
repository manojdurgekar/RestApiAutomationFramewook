from config import LOG
from config import Hide_sensitive_data
#we will build the request headers 

def build_requests_header(access_token, accept_type="application/json", **kwargs):

    LOG.info("build_request_headers")
    headers = {
        "Authorization": f"Bearer {login_as_admin}",
        "Accept": accept_type
    }

    if "content_type" in kwargs:
        headers["Content-Type"] = kwargs["content_type"]
    
    LOG.debug(f"Request headers:{headers}")
    return headers