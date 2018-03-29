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
