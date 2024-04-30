from LESSON_15.bank import Banknote
from LESSON_15.custom_iterator import CustomIterator


class Wallet:

    def __init__(self, *banknotes: Banknote):
        self.container = []
        self.container.extend(banknotes)

    def __repr__(self):
        return f'Wallet({self.container})'

    def __contains__(self, item): # in
        return item in self.container

    def __bool__(self):
        return len(self.container) > 0

    def __len__(self):
        return len(self.container)

    def __call__(self):
        total = 0
        for money in self.container:
            total += money.value
        return total

    def __iter__(self):
        return CustomIterator(self.container)

    def __getitem__(self, item: int):
        if item > len(self.container):
            return False
        return self.container[item]

    def __setitem__(self, key, value):
        self.container[key] = value


if __name__ == '__main__':
    wallet = Wallet(Banknote(500), Banknote(100))
    for money in wallet:
        print(money)