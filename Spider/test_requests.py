# test requests

import requests

response = requests.get('http://www.baidu.com')\
# 未经过js渲染的源代码
print(response.text)

print(response.headers)
print(response.status_code)
print(response.cookies)

# 经过js渲染的源代码
# from selenium import webdriver
# 需要添加chrome驱动
# driver = webdriver.Chrome()
# driver.get('http://www.taobao.com')
# print(driver.page_source)

# =============  get请求

# 基本get请求
response = requests.get('http://httpbin.org/get')
print(response.text)

# 带参数get请求
response = requests.get('http://httpbin.org/get?name=wangchuan&age=21')
print(response.text)

data = {
    'name': 'wangchuan',
    'age': 21
}
response = requests.get('http://httpbin.org/get', params=data)
print(response.text)

# 解析json
response = requests.get('http://httpbin.org/get')
print(type(response.text))  # == import json  print(json.loads(response.text))
print(response.json())
print(type(response.json()))

# 获取二进制数据  (保存github的图标)  content
response = requests.get('https://github.com/favicon.ico')
print(type(response.text), type(response.content))
# print(response.text)
print(response.content)
with open('favicon.ico', 'wb') as f:
    # 保存在项目根目录下
    f.write(response.content)
    f.close()

# 添加headers
response = requests.get('https://www.zhihu.com/explore')
# <html><body><h1>500 Server Error</h1>
#   An internal server error occured.
#   </body></html>
print(response.text)

# 必须要添加headers
headers = {'User-Agent': ''}
response = requests.get('https://www.zhihu.com/explore', headers=headers)
print(response.text)


# ============= post请求

# 基本post请求
data = {'name': 'wangchuan', 'age': 22}
response = requests.post('http://httpbin.org/post', data=data)
print(response.text)


# ============= response属性
response = requests.get('http://www.jianshu.com')
print(type(response.status_code), response.status_code)
print(type(response.headers), response.headers)
print(type(response.cookies), response.cookies)
print(type(response.url), response.url)
print(type(response.history), response.history)

exit() if not response.status_code == requests.codes.ok else print('Request Successfully')
exit() if not response.status_code == 200 else print('Request Successfully')

# ============== 高级操作

# 文件上传 post请求
file = {'upload_file': open('favicon.ico', 'rb')}
response = requests.post('http://httpbin.org/post', files=file)
print(response.text)

# 获取cookies
response = requests.get('https://www.baidu.com')
print(response.cookies)
for key, value in response.cookies.items():
    print(key + '=' + value)

# 会话维持 (模拟登陆)
# 反例
requests.get('http://httpbin.org/cookies/set/number/123456789')
response = requests.get('http://httpbin.org/cookies')
print(response.text)

session = requests.Session()
session.get('http://httpbin.org/cookies/set/number/123456789')
response = session.get('http://httpbin.org/cookies')
print(response.text)