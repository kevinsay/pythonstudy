class Dog:
    def __init__(self, name):
        self.name = name
        pass

    def eat(self):
        print("%s is eating" % self.name)


def bulk(self):
    print('1234')


dog = Dog("dahuang")
choice = input(">>:").strip()
if hasattr(dog, choice):
    func = getattr(dog, choice)
    func()
else:
    setattr(dog,choice,bulk)
    func = getattr(dog, choice)
    func(dog)


print('111111111111111')
print('111111111111111')
print('222222222222222')
print('333333333333333')
print('444444444444444')
