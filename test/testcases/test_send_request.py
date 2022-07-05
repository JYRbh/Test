import json

import pytest
import requests

#####
from common.requests_util import RequestsUtil
from common.yaml_util import YamlUtil


class TestSendRequest:

    #类变量：通过类名来访问
    #access_token= ""

    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('get_token.yml'))
    def test_get_token(self,caseinfo):
        print(caseinfo['name'])
       # print (caseinfo['validate'])
        #发送get请求#
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        result = RequestsUtil().send_request(method,url,data)
        #result = TestSendRequest.request(method,url = url,params = data)
        result = json.loads(result)
        print(result)

        if 'access_token' in result:
            YamlUtil().write_extract_yaml({'access_token':result['access_token']})
            assert 'access_token' in result
        else:
            assert result['errcode'] == 40002
        #TestSendRequest.access_token = rep.json()['access_token']

    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('edit_flag.yml'))
    def test_edit_flag(self,caseinfo):
        method = caseinfo['request']['method']
        access_token = YamlUtil().read_extract_yaml('access_token')
        url = caseinfo['request']['url']+"?access_token="+access_token+""
        data = caseinfo['request']['data']
        # 发送post请求（data和json只需要传一个）
        #rep =TestSendRequest.session.request(method,url,json=data)
        result = RequestsUtil().send_request(method,url,data)
        result = json.loads(result)

        print(result)
        #assert result['errcode'] == 0
#
#     def test_access_token(self):
#         print(TestSendRequest.access_token)
#
#
# #AppID(小程序ID)
# #-s :表示输出调试信息，包括prin打印的信息
#
# #-v :显示更详细的运行信息
#
# #-vs:这两个参数可一起使用
# #####