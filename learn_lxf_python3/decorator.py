def now():
    print('2018-3-28')

f = now
f()

print(f.__name__, now.__name__)