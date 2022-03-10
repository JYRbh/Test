from  selenium import webdriver
from time import sleep
import pickle
#主页
damai_url = 'https://www.damai.cn/'

#登录
login_url = 'https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F'

#目标抢票的界面
target_url = 'https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.25934d15pgL78r&id=666239492879&clicktitle=%E6%A5%A0%E6%BA%AA%E6%B1%9F%C2%B7%E6%98%9F%E5%B7%A2%E7%A7%98%E5%A2%83%E9%9F%B3%E4%B9%90%E8%8A%82ROCKTOWN'

class Concert:
    #完成一个初始化
    def __init__(self):
        self.status = 0 #状态码，表示当前执行到了哪个步骤
        self.login_method = 1 #{0:模拟登录，1：免登录}
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')

    def set_cookies(self):
        """登录网址的时候要用的方法"""
        self.driver.get(damai_url)
        print("###请点击登陆###")
        #如果说我一直没有点击登陆？
        while self.driver.find('大麦网-全球演出赛事官方购票平台')!= -1:
            sleep(1)
        print("###扫描成功###")
        pickle.dump(self.driver.get_cookies(),open('cookies.pkl','wb'))    # 保存cookie
        print('###cookie保存成功###')
        self.driver.get(target_url)

    def get_cookie(self):
        """假如我现在已经登陆过了 那么直接拿"""
        cookies = pickle.load(open('cookies.pkl','rb'))
        for cookie in cookies:
            cookie_dict = {
                'domain':'.damian.cn',
                'name':cookie.get('name'),
                'value':cookie.get('value')
            }
            self.driver.add_cookie(cookie_dict)
        print('###载入cooki###')

    def login(self):
        """登陆"""
        if self.login_method == 0


