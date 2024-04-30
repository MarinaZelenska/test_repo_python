class Banknote:

    def __init__(self, value: int):
        self.value = value

    def __str__(self):
        return f'{self.__class__.__name__} with {self.value} EUR'

    def __repr__(self):
        return f'Banknote({self.value})'

    def __eq__(self, other):
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value == other.value

    def __lt__(self, other):  # less than
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value < other.value

    def __le__(self, other):  # less equal
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value <= other.value

    def __gt__(self, other):  # greater than
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value > other.value

    def __ge__(self, other):  # greater equal
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value >= other.value
