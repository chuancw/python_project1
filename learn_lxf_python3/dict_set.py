# dict 字典  键值对

d = {'Michal': 95, 'Bob': 75, 'Emind': 100}
print(d['Emind'])
d['Michal'] = 80
print(d['Michal'])
print(d.get('Michal'))

# 删除key
print(d.pop('Michal'))
print(d)

print('**************************')

# set 是key的集合  不重复  必须是不可变对象


s1 = set([1,2,3,4,5])
print(s1)
s1.add(8)
print(s1)
s1.remove(3)
print(s1)


# 不可变对象
a = 'abc'
b = a.replace('a', 'A')
print(b)
print(a)