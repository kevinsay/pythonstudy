class Dog:
    def __init__(self, name):
        self.name = name
        self.data = {}

    @staticmethod
    def run(self):
        print('11111')

    def __call__(self, *args, **kwargs):
        print('dog is running')

    def __str__(self):
        return 'dsdsds'

    def __setitem__(self, key, value):
        self.data[key] = value
        print('__setitem__,%s:%s' % (key, value))

    def __delitem__(self, key):
        pass

    def __new__(cls, *args, **kwargs):
        print('__new__')
        return object.__new__(cls)


dog = Dog('123')
print(dog)
# print(dog.__module__)
# print(dog.__class__)
# print(dog.__dict__)
# print(Dog.__dict__)
# print(dog)
# dog['name'] = 'syt'
# print(dog.data)

# def func(self):
#     print('123')
#
# Foo = type('Foo',(),{'func':func})
#
# f = Foo()
# f.func()
