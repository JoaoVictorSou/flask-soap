from flask import request
from bs4 import BeautifulSoup

class Soap(object):
    def __init__(self, app):
        self._app = app

    def deserialize(self):

        with self._app.app_context():
            headers = request.headers
            body = request.data
        
        xml_request = BeautifulSoup(body, features='xml')
        
        print(xml_request.find('soapenv:Envelope'))