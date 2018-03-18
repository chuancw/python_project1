from urllib import request
from urllib import error

if __name__ == '__main__':

    # 一个不存在的链接
    url = 'http://www.sdhfjkshfjksd.com'

    try:
        response = request.urlopen(url)
        html = response.read().decode('UTF-8')
        print(html)

    except error.URLError as e:
        print(e.reason)

    url2 = 'http://www.douyu.com/Jack_Cui.html'

    try:
        response = request.urlopen(url2)
        html = response.read()

    except error.HTTPError as e:
        print(e.code)


    # 如果想用HTTPError和URLError一起捕获异常，那么需要将HTTPError放在URLError的前面
    # HTTPError是URLError的子类


    print('===============================')
    url3 = 'http://www.bdfdu.com/sdfsdf_sdfgsf.html'

    try:
        response = request.urlopen(url3)
        html = response.read()

    except error.URLError as e:
        print(e)
        if hasattr(e, 'code'):
            print('HTTPError: ', e.code)
        if hasattr(e, 'reason'):
            print('URLError: ', e.reason)


