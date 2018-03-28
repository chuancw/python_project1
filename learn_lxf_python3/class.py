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