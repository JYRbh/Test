from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import pickle
import os
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
        s = Service("chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)

    def set_cookies(self):
        """登录网址的时候要用的方法"""
        self.driver.get(damai_url)
        print("###请点击登陆###")
        #如果说我一直没有点击登陆？
        while self.driver.title.find('大麦网-全球演出赛事官方购票平台')!= -1:
            sleep(1)
        while self.driver.title != '大麦网-全球演出赛事官方购票平台-100%正品、先付先抢、在线选座！':
            sleep(1)
        print("###扫描成功###")
        #get_cookies:driver里面的方法
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
        """登录"""
        if self.login_method == 0:
            self.driver.get(login_url)
            print('###开始登录###')
        elif self.login_method == 1:
            #创建文件夹，文件是否存在
            if not os.path.exists('cookies.pkl'):
                self.set_cookies()        #没有文件的情况下，登录一下
            else:
                self.driver.get(target_url)   #跳转到抢票页
                self.get_cookie()             #并且登录

        def enter_concert(self):
            """打开浏览器"""
            print('###打开浏览器，进入大麦网###')
            #调用登录
            self.login()            #先登录再说
            self.driver.refresh()   #刷新页面
            self.status = 2         #登录成功标识
            print('###登录成功###')

if __name__ == '__main__':
    con = Concert()
    con.login()


