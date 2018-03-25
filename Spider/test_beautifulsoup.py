from bs4 import BeautifulSoup

html = '''
<html><head><title>The Emind's story</title></head>
<body>
<p class="title" name="Emind"><b>The Emind's story</b></p>
<p class="story">fasdf ajfsdkl adf ria df jl;sdffjsfd
<a href="http://sdfdsf.com" class="sister" id="link1"><!--df --></a>
<p class="story">.....</p>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title.string)

print(soup.title)
print(soup.head)
print(soup.p)   # 输出了第一个p标签

print(soup.title.name) # 输出标签的名称

