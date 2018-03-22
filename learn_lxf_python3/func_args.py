
# 设置默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s*x
    return s

print(power(5))
print(power(5,3))


def enroll(name, gender, age=6, city='xian'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('wangchuan', 'F')
enroll('wangchuan', 'M', age=21)
enroll(name='wangchuan', gender='HH', city='beijing')

def add_end(L=[]):
    L.append('END')
    return L

print(add_end())
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
print(add_end())


def add_end_new(L=None):
    if L is None:
        L = []

    L.append('END')
    print(L)

add_end_new()
add_end_new()


# ======设置可变参数

# 传入list或者tuple
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(sum)

calc([1,2,3])
calc((1,2,3))

# 利用可变参数
def calc_change(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(sum)
calc_change(1,2)
calc_change()

nums = [1,2,3]
calc_change(*nums)

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('wangchuan', 22)
person('wangchuan', 22, key='after', city='beijing')
data = {'city:' 'beijing', 'job:' 'soft'}
person('wangchuan', 22, **data)