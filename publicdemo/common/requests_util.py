import pytest
import requests


class RequestUtil():

    session = requests.session()

    def send_request(self,method,url,data,**kwargs):

        method =str(method).lower()
        res = ''
        if method =="get":
            res = RequestUtil.session.request(method,url,params=data,**kwargs)
        elif method == "post":
            res =RequestUtil.session.request(method,url,json=data,**kwargs)

        return res






