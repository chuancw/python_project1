from urllib import request

if __name__ == '__main__':

    #没有设置data参数，是get方式获取数据
    response = request.urlopen('http://fanyi.baidu.com')
    print('geturl打印信息：', response.geturl())
    print('info 打印信息：', response.info())
    print('getcode打印信息： ', response.getcode())




