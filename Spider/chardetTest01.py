import chardet
from urllib import request

# 获取网页的编码方式

if __name__ == '__main__':
    response = request.urlopen('http://www.baidu.com')
    html = response.read()

    # 使用http 能查看到网页编码  https不能看到
    charset = chardet.detect(html)
    print(charset)



