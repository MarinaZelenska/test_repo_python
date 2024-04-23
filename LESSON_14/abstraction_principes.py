from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    @abstractmethod
    def do_work(self):
        pass

    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):

    def __init__(self, name, position, salary):
        super().__init__(name, position, salary)
        self.bonus = 50

    def do_work(self):
        print("I do work like Manager")

    def calculate_salary(self) -> int:
        return (self.salary * self.bonus // 100) + self.salary


if __name__ == '__main__':
    maryna = Manager("Maryna", "Manager", 4000)
    maryna.do_work()
    print(maryna.calculate_salary())
