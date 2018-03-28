def cal_sum(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum

print(cal_sum(1, 2, 3, 4))

# 返回函数
def lazy_sum(*args):
    def get_sum():
        sum = 0
        for n in args:
            sum = sum + n
        return sum
    return get_sum

f = lazy_sum(1,2,3,4,5)
f_test = lazy_sum(1,2,3,4,5)
print(f)
print(f())
print(f == f_test)