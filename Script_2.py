from abc import abstractmethod


class Dress:
    @abstractmethod
    def calculation(self):
        pass


class Coat(Dress):
    def __init__(self, V):
        self.V = V

    @property
    def calculation(self):
        parameter = self.V
        return parameter / 6.5 + 0.5


class Costume(Dress):
    def __init__(self, H):
        self.H = H

    @property
    def calculation(self):
        parameter = self.H
        return parameter * 2 + 0.3


my_coat = Coat(2)
my_costume = Costume(5)
print(my_coat.calculation)
print(my_costume.calculation)
