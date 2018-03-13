# list里面的元素数据类型可以不同
classmates = ['wangchuan', 'chenhao', 'Emind']
print(classmates)
print(len(classmates))
print(classmates[0])

# 遍历元素
for name in classmates:
    print(name)

print(classmates[-1])

# 追加元素
classmates.append('Adam')
print(classmates[3])

classmates.insert(1, 'Jack')
print(classmates)

# 删除list末尾的元素
print(classmates.pop())
print(classmates)

# 删除指定位置的元素
print(classmates.pop(1))
print(classmates)

testlist = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(testlist))

print('****************** next is tuple ************')
# tuple 不可变
tuple1 = ('A', 'B', 'C')
print(tuple1)

# 定义一个元素的tuple
# not  t = (1)
t = (1, )
print(t)

