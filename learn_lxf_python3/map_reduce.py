
# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
from functools import reduce


def f(x):
    return x * x

r = map(f,list(range(10)))
print(list(r))

print(list(map(str, list(range(10)))))


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
# 这个函数必须接收两个参数
# reduce把结果继续和序列的下一个元素做累积计算

def add(x , y):
    return x + y

print(reduce(add, list(range(10))))
print(sum(list(range(10))))