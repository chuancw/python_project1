print(abs(-100))

print(max(1,2,3,4, -1))

print(bool(1))
print(int('1234'))

a = abs
print(a(-10000))

# 定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-24))

# 空函数
def loop():
    pass

# 空语句
if 10 > 12:
    pass


# 增加参数校验
def my_abs_1(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad args')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs_1(-122))
print(my_abs_1('231'))

# 函数可以返回多个值， 实际上是一个tuple