from types import MethodType


class Student(object):
    pass

s = Student()
# 给实例绑定属性
s.name = 'Emind'
print(s.name)

def set_age(self, age):
    self.age = age

# 给实例绑定方法
s.set_age = MethodType(set_age, s)
s.set_age(21)
print(s.age)

# 其他实例不起作用，就需要给class绑定方法
Student.set_age = set_age
s2 = Student()
s2.set_age(100)
print(s2.age)


# ============= 限制实例的属性 __slots__ ============
class Teacher(object):
    __slots__ = ('name', 'age')


teacher = Teacher()
teacher.name = 'wangchuan'
teacher.age = 21
# teacher.score = 150