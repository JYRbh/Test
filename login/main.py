
import urllib.request

# neirong = urllib.request.urlopen("http://www.baidu.com")
# webfile = neirong.read()
# print(webfile)
# f = open("1.html","wb")
# f.write(webfile)
# f.close()

# url = "https://www.baidu.com/"
# headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36")
# opener = urllib.request.build_opener()
# opener.addheaders =[headers]
# data = opener.open(url).read()
#
# print(data)

# url = "https://www.baidu.com/"
# opener = urllib.request.build_opener()
# data = opener.open(url).read()


keywd = "hello"
url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd="
key = "哈哈哈"
key_code = urllib.request.quotoe(key)
url_all = url + key_code
req = urllib.request.Request(url_all)
data = urllib.request.urlopen(req).read()
fhandle = open("1.html","wb")
fhandle.write(data)
fhandle.close()