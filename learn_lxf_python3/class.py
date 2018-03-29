class student(object):

    # 构造函数
    def __init__(self,name,score):
        self.name = name
        self.score = score

    # 在类中定义的函数只有一点不同
    # 就是第一个参数永远是实例变量self
    # 并且，调用时，不用传递该参数
    def print_attr(self):
        print('%s, %s' % (self.name, self.score))


Tom = student('Tom', 100)
Tom.print_attr()

# 可以自由地给一个实例变量绑定属性
Tom.age = 21
print(Tom.age)


# 访问限制
class Teacher(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print(self):
        print(self.__name, self.__age)

    def get_name(self):
        print(self.__name)

    def get_age(self):
        print(self.__age)

    def set_age(self, age):
        if 0 <= age <= 100:
            self.__age = age
        else:
            raise ValueError('bad age')

teacher = Teacher('Hu', 40)
# print(teacher.__name)
teacher.print()
teacher.get_age()
teacher.get_name()
teacher.set_age(10)
teacher.get_age()
# teacher.set_age(-1)