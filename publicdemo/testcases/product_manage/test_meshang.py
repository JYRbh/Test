import time

from common.common import CommonUtil


class TestMashang(CommonUtil):

    def test_baili(self):
        print("测试百里老师")
        assert 1==1

    def test_xingyao(self,login,pm):
        print("测试星瑶老师"+login+pm)
        assert 'a' in 'abc'

    def test_yiran(self):
        print("测试依然老师")
        flag = True
        assert flag is True

class TestJiaoyu:
    def test_01_mashang(self):
        print("码尚教育")