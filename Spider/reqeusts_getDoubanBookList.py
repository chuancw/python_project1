import requests
import re

# resp.text返回的是Unicode型的数据。
# 使用resp.content返回的是bytes型的数据。
# 也就是说，如果你想取文本，可以通过r.text。
# 如果想取图片，文件，则可以通过r.content

content = requests.get('https://book.douban.com').text

pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title.*?"(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
pattern_test = re.compile('<li.*?more-meta.*?author">(.*?)</span>.*?</li>', re.S)
text = re.findall(pattern_test, content)
for author in text:
    print(author.strip())
results = re.findall(pattern, content)
print(results)
for result in results:
    url, name, author, date = result
    print(url, name, author, date)

