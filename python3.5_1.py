import sys
print(sys.path)

print(type('hello'))
a='a'
b=a
a='A'
print(b)

L1=[1,2,3]
L2=[2,3,4]
print(L1+L2)




print(5 in L1)

greeting='hello,world'
print('w' in greeting)


print(len(L2))
print(max(L2))
print(min(L2))

L1.extend(L2)
print(L1)


print(L2.count(2))
print(L1.count(2))

print(L1.index(2))
print(L1[2])
print(L1)
print(L1.sort())
print(L1)

L1.clear()
print(L1)


filed=('hello','world','fujiu','tudou')
print(filed[2])
print(filed[-1])

name='niha'
slution='huju'
print(name,slution)

print(name[-1:])


detail=dict(name='Jack',age=16)
print(detail)
print(detail['name'])

from math import pi
print(pi)

import math as m
print(m.pi)

x,y,z=1,2,3
print(x,y,z)
student = {'name':'Json', 'number':'1001'}
key,value = student.popitem()
print(key,value)

K1=[1,2,3]
K2=[1,2,3]
print(K1 == K2)
print(K1 is K2)

num = 7
if 5<= num <= 10:
    print('num的值在5到10之间',num)
else:
    print('else')

if 5<=num and num<=10:
    print('1')
else:
    print('2')

test1=[1,2,3,4,5]
for x in test1:
    print(x)

tups={'name':'nihao','age':'18'}
for y in tups:
    print(y,tups[y])

#print(tups.items())
for key,value in tups.items():
    print(key,value)

student1=['wangchuan','xiaoqiang','xiaozhi']
number=[1001,1002,1003]
for name,num in zip(student1,number):
    print(name, num)


for num1,num2 in zip(range(3),range(100)):
    print(num1, num2)

sort1=[6,7,8,1,2]
print(sorted(sort1))
print(sort1)

def personInfo(name,age):
    print('name=',name)
    print('age=',age)

personInfo(age=16,name='nihao')

def personInfo1(name,age=16):
    print('name=',name)
    print('age=',age)
personInfo1('wangchuan')

def personInfo2(name,*vartuple):
    print(name)
    for var in vartuple:
        print(var)
personInfo2('wangchuan',12,3,4,5,'322')
testlist1=[1,2]
testtuple1=(1,2)
personInfo2('wangchaun',testlist1)
personInfo2('nihao',testtuple1)

total=100
def print_total():
    print('total is； ', total)
print_total()

totalnum=2000
print('before is : ', totalnum)

def func():
    #global totalnum = 200   error
    global  totalnum
    totalnum=200
    print('the func is : ', totalnum)
func()
print('after is :', totalnum)

def sum_late(*args):
    def calc_num():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return calc_num
f=sum_late(12,3,4)
print(f())


def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs   #返回3个函数

f1,f2,f3=count()
print(f1(),f2(),f3())

def getsum(x,y):
    return x+y
print(getsum(1,2))


#匿名函数
LL1=[1,2,3,4,5]
LL2=[]
for i in LL1:
    if i>3:
        LL2.append(i)
print(LL2)

def func1(x):
    return x>3
f_list=filter(func1,[1,2,3,4,5])
print([item for item in f_list])

print([item for item in filter(lambda x:x>3,[1,2,3,4,5,6])])





