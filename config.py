from operator import truediv
import requests
import logging

SESSION = requests.Session()

APP_URL = "http://localhost:8080"

ADMIN_USER = "admin"
ADMIN_PASSWORD ="admin"


#Globballog variable 
LOG = logging .getLogger()

#wrapper class to hide password 

class Hide_sensitive_data(logging.Filter):
    
    def filter(self,record):
        record.msg = str(record.msg).replace("ADMIN_PASSWORD","*******")
        return true

LOG.addFilter(Hide_sensitive_data())
