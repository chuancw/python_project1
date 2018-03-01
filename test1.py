import os
print(os.path)


def hello(name):
    return 'Hello, '+name+'!'

print(hello('wangchuan'))

def doc(x):
    'this is a function doc'
    print(x)

print(doc.__doc__)


name=['list1','list2']
def change_name(name):
    name[0]='list0'
    name[1]='list1'

change_name(name)
print(name)

def inc(x):
    return x+1

f=10
f=inc(f)
print(f)

def hello_1(greeting,name):
    print('%s,%s!' %(greeting,name))
hello_1('hello','world')