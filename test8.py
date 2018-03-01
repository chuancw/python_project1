class MyClass(object):

    i=123
    def func(self):
        print('hello world')

myclass1=MyClass()
print(myclass1.i)
myclass1.func()

class MyClass2(object):
    i=123
    def __init__(self,name):
        self.name=name

    def f(self):
        print(self.i, self.name)
myclass2=MyClass2('wangchuan')
print(myclass2.name , myclass2.i)

class DefaultInit(object):
    def __init__(self):
        print('this is a init function')

    def show(self):
        print('this is a function')

test=DefaultInit()
test.show()

class Student1(object):
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def set_age(self,age):
        self.__age=age

    def get_age(self):
        print(self.__age)

student1=Student1('wangchuan',100)
student1.set_age(100)
student1.get_age()


class Student0(object):
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name

print(Student0('wangchuan'))

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self


    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a>100:
            raise StopIteration
        return self.a

for n in Fib():
    print(n)




def exception_exp(x,y):
    try:
        a=x/y
        print(a)
        return a
    except Exception:
        print('出现异常....')

exception_exp(10,0)







