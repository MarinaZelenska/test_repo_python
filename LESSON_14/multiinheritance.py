class Father:

    def __init__(self):
        self.strength = 40

    def do_workout(self):
        return f'Do workout with strenght {self.strength}'


class Mother:

    def __init__(self):
        self.wisdom = 60

    def read_books(self):
        return f'Read books with wisdom {self.wisdom}'


class Child(Father, Mother):

    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def play(self):
        return "I play"


if __name__ == '__main__':
    tom = Child()
    print(tom.do_workout())
    print(tom.read_books())
    print(tom.play())
    print(Child.mro())
