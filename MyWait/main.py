# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import urllib.request
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = '111.229.161.172:888'
proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'http://' + proxy,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
})
request = urllib.request.build_opener(proxy_handler)

try:
    response = request.open('https://www.baidu.com/')

    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)



'''
import requests

proxy = '111.229.161.172:888'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}
try:
    response = requests.get('https://www.baidu.com/',proxies = proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)
'''
