from bs4 import BeautifulSoup

html = '''
<html><head><title>The Emind's story</title></head>
<body>
<p class="title" name="Emind">
   <b>The Emind's story</b>
   <a href='http://chuancw.com" id="id1">
     <span>ELSe</span>
   </a>
</p>
</p>
<p class="story">fasdf ajfsdkl adf ria df jl;sdffjsfd
<a href="http://sdfdsf.com" class="sister" id="link1"><!--df --></a>
<p class="story">.....</p>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title.string)


# 选择元素
print(soup.name)
print(soup.title)
print(soup.head)
print(soup.p)   # 输出了第一个p标签

# 输出标签的名称
print(soup.title.name)

# 获取属性
print(soup.p['name'])

# 获取内容
print(soup.p.string)

# 嵌套选择
print(soup.title.string)
print(soup.head.title.string)


# 子节点和子孙节点
print(soup.p.contents)
print('=========================')
# 子节点
print(soup.p.children)
for i, children in enumerate(soup.p.children):
    print(i, children)

# 子孙节点
print(soup.p.descendants)
for i, descendants in enumerate(soup.p.descendants):
    print(i, descendants)
