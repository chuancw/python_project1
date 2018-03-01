from urllib import request
from urllib import parse
import json

if __name__ == "__main__":
    # Request URL     去掉_o
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # 创建Form_Data字典，存储上图的Form Data
    data = {}

    data['i'] = 'content'
    data['from'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1519913979709'
    data['sign'] = '1357b6e436861f0109278f22739c7733'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CL1CKBUTTON'
    data['typoResult'] = 'false'

    # 使用urlencode方法转换标准格式
    data = parse.urlencode(data).encode('utf-8')
    print(data)
    # 传递Request对象和转换完格式的数据
    response = request.urlopen(Request_URL, data)
    # 读取信息并解码
    html = response.read().decode('utf-8')
    print(html)
    # 使用JSON
    translate_results = json.loads(html)

    # 找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']

    # 打印翻译信息
    print("翻译的结果是：%s" % translate_results)