import re

# ======= match =========  开头匹配


  # 总结：尽量使用泛匹配
  #      使用括号得到匹配目标
  #      尽量使用非贪婪模式
  #      有换行符就用re.S

# 最常规的匹配
content = 'Hello 123 4567 World_This is a Regex Demo'

result = re.match('^Hello\s\d+\s\d{4}\s\w{10}.*Demo$', content)
print(result)
print(result.group())
print(result.span())


# 泛匹配
result = re.match('^Hello.*Demo$', content)
print(result.group())


# 匹配目标
content1 = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld.*Demo$', content1)
print(result.group())
print(result.group(1))


# 贪婪匹配
result = re.match('^He.*(\d+).*Demo$', content1)
print(result.group())
print(result.group(1))  # 只匹配到7 .*会覆盖最后一个数字前的数字


# 非贪婪匹配
result = re.match('^He.*?(\d+).*Demo$', content1)
print(result.group(1))


# 匹配模式
content2 = '''Hello 1234567 World_This
is a Regex Demo
'''
result = re.match('^He.*?(\d+).*Demo$', content2)
print(result)  # None  .*不能匹配换行符

result = re.match('^He.*?(\d+).*Demo$', content2, re.S)
print(result)
print(result.group(1))


# 转义
content3 = 'price is $5.00'
result = re.match('price is $5.00', content3)
print(result)  # None 需要转义

result = re.match('price is \$5\.00', content3)
print(result.group())



# ======= search =======  不需要从开头进行匹配

content4 = 'Extra strings Hello 1234567 World_This is a Regex Demo Strings'
result =re.search('Hello', content4)
print(result.group())

# findall 找所有的
content5 = 'My Hello Hello 1234'
result = re.findall('Hello', content5)
print(result)
for x in result:
    print(x)

# sub 替换字符串
result = re.sub('\d+', '0000', content4)
print(result)

# =========== compile ======= 编译
content_compile = 'Hello 1234567 Demo'
pattern = re.compile('Hello.*Demo', re.S)
result = re.match(pattern, content_compile)
print(result.group())