class Student(object):

    name = 'Student'

    def __init__(self, name):
        self.name = name


s = Student('wangchuan')
print(s.name)
print(Student.name)
