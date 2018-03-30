class Animal(object):

    def run(self):
        print('animal is running')


class Dog(Animal):
    def run(self):
        print('Dog is running')

class Cat(Animal):
    pass

dog  = Dog()
dog.run()

cat = Cat()
cat.run()

def run_test(animal):
    animal.run()

run_test(Animal())
run_test(Dog())

print(type(123) == int)

# 获取一个对象的所有属性和方法
print(dir(dog))
print(dir(Animal))
print('ABC'.lower())



# 测试对象属性
class myObject(object):

    def __init__(self):
        self.x = 99

    def power(self):
        return self.x * self.x

obj = myObject()
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
# 设置一个属性
setattr(obj, 'name', 'wangchuan')
print(hasattr(obj, 'name'), obj.name)
#  传入default参数，属性不存在，返回默认值
print(getattr(obj, 'z', 404))



