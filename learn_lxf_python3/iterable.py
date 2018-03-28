from collections import Iterable, Iterator

# 直接作用于for循环的对象统称为可迭代对象：Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance(100, Iterable)) # False


# 以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
print(isinstance([], Iterator)) # False
print(isinstance(iter([]), Iterator))

# Python的for循环本质上就是通过不断调用next()函数实现的