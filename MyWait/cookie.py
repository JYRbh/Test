import webbrowser

import requests
from urllib.parse import urljoin

from selenium.webdriver.chrome.service import Service

base_URL='https://login2.scrape.center/'
login_URL = urljoin(base_URL,'/login')
index_URL = urljoin(base_URL,'/page/1')
username = 'admin'
password = 'admin'

response_login = requests.post(login_URL,date={
    'username':username,
    'password':password

})

response_cookies = response_login.cookies

response_index = requests.get(index_URL,cookies=response_cookies)

s = Service("chromdriver.exe")
driver = webbrowser.Chrome(service = s,cookies = response_cookies)




