class Animal:

    def make_noize(self):
        return 'Make noize'


class Cat(Animal):

    def make_noize(self):
        return 'Make noize - meow'


class Dog(Animal):

    def make_noize(self):
        return 'Make noize - bark'


class Car:
    def make_noize(self):
        return 'Make noize - car'


def noize(animal: Animal):
    return animal.make_noize()


if __name__ == '__main__':
    print(noize(Cat()))
    print(noize(Dog()))
    print(noize(Car()))

    print(1 + 1)
    print('1' + '1')
    print([1, 2, 3] + [5, 6, 7])
