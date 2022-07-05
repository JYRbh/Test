import pytest

from common.common import CommonUtil
from common.yaml_util import read_yaml


class TestApi(CommonUtil):

    @pytest.mark.parametrize('caseinfo',read_yaml("testcases/user_manage/get_token.yaml"))
    def test_01_get_token(self,caseinfo):
        print("获取统一接口鉴权码"+str(caseinfo))