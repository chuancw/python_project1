l = [x * x for x in range(10)]
print(type(l), l)

# 一个generator
l2 = (x * x for x in range(10))
ll = list(l2)
print(type(ll), ll)
print(type(l2), l2)
for i in l2:
    print(i)


def fib(count):
    n, a, b = 0, 0, 1
    while n < count:
        a, b = b, a+b
        n = n + 1
        yield n
    return 'done'
f = fib(5)
for i in f:
    print(i)