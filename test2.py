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
