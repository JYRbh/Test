import pytest

class TestApi:

    @pytest.mark.parametrize('args',['百里','星瑶','依然'])
    def test_api(self,args):
        print(args)

    @pytest.mark.parametrize('name,age',[['百里',13],['呈瑶',10]])
    def test_api2(self,name,age):
        print(name,age)

    @pytest.mark.parametrize('args',[['百里',13],['呈瑶',10]])
    def test_api3(self,args):
        print(args)
if __name__=='__main__':
    pytest.main(['-vs','test_api.py'])
