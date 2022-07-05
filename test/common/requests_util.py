import json

import requests


class RequestsUtil:

    #类变量：通过类名访问
    session = requests.session()

    def send_request(self,method,url,data,**kwargs):
        method = str(method).lower()
        rep = None
        if method == 'get':
            rep = RequestsUtil.session.request(method,url=url,params=data,**kwargs)
        else:
            data = json.dumps(data)
            rep = RequestsUtil.session.request(method, url=url, data=data, **kwargs)
        return rep.text

