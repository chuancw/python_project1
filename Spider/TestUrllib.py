import urllib
from urllib import request


response = request.urlopen('https://www.baidu.com')
print(response)
print(response.read())

print('==================================')

if __name__ == '__main__':
    response2 = request.urlopen('https://www.baidu.com')
    html = response2.read()
    html = html.decode('UTF-8')
    print(html)
