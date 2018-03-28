def filter_func(n):
    return n % 2 == 0

l = list(filter(filter_func, list(range(10))))
print(l)