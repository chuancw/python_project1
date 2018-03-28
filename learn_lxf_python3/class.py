class student(object):

    # 构造函数
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_attr(self):
        print('%s, %s' % (self.name, self.score))


Tom = student('Tom', 100)
Tom.print_attr()


Tom.age = 21
print(Tom.age)