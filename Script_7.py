class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.number = f'{a}+{b}i'

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'{self.a * other.a - (self.b * other.b)} + {self.a * other.b + self.b * other.a}i'


my_ComplexNumber = ComplexNumber(2, -2)
my_ComplexNumber_2 = ComplexNumber(1, 1)
print(my_ComplexNumber + my_ComplexNumber_2)
print(my_ComplexNumber * my_ComplexNumber_2)
