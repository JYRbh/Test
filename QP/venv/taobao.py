import json
from time import sleep
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pickle
import os
import utllib.request


#主页
damai_url = 'https://www.taobao.com'

#登录
login_url = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.jianhua.201864-2.d1.5af911d9w9erLt&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F'

#目标抢票的界面
target_url ='https://item.taobao.com/item.htm?spm=a21bo.jianhua.201876.1.5af911d9fwMmVG&id=37746780650&scm=1007.34127.211940.0&pvid=1642927e-dd3e-4ba0-9b1c-b465a158ed70&mt='


class Taobao:
    #完成一个初始化
    def __init__(self):
        self.status = 0 #状态码，表示当前执行到了哪个步骤
        self.login_method = 1 #{0:模拟登录，1：免登录}
        s = Service("chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)

        #打开信息平台登录界面

    def set_cookies(self):
        """登录网址的时候要用的方法"""
        self.driver.get(login_url)
        while str(self.driver.current_url) == login_url:
            sleep(1)
        print("###扫描成功###")
        # get_cookies:driver里面的方法
        pickle.dump(self.driver.get_cookies(), open('cookies.pkl', 'wb'))  # 保存cookie
        print('###cookie保存成功###')
        self.driver.get(target_url)

    def get_cookie(self):
        """假如我现在已经登陆过了 那么直接拿"""
        cookies = pickle.load(open('cookies.pkl', 'rb'))
        for cookie in cookies:
            cookie_dict = {
                'domain': '.taobao.com',
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                'path':'/',
                'expires':None
            }

            self.driver.add_cookie(cookie_dict)
        print('###载入cooki###')
        sleep(2)
        self.driver.get(target_url)

        sleep(5)
        self.driver.find_element(By.XPATH,'/html/body/div[12]/div[2]/div').click()

    def login(self):
        if self.login_method == 0:
            self.driver.get(damai_url)
            print('###开始登录###')
        elif self.login_method == 1:
            #创建文件夹，文件是否存在
            if not os.path.exists('cookies.pkl'):
                self.set_cookies()        #没有文件的情况下，登录一下
            else:
                self.driver.get(target_url)   #跳转到抢票页
                self.get_cookie()             #并且登录
        driver = webdriver.Chrome()
        driver.maximize_window()

    def enter_concert(self):
        """打开浏览器"""
        self.login()  #点击登录
        self.driver.refresh() #刷新页面

    def isElementExisr(self,element):
        """"判断元素是否存在"""
        flag = True
        browser = self.driver
        try:
            browser.find_element(By.XPATH,'element')
            return  flag
        except:
            flag = False
            return flag


if __name__ == "__main__":
    taobao = Taobao()
    taobao.login()


