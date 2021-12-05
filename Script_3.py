class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        result = self.count - other.count
        if result >= 0:
            return result
        else:
            return 'Разность числа клеток меньше нуля'

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count // other.count

    def __mod__(self, other):
        return self.count%other
    def make_order(self, class_cell, count):
        result = ''
        for i in range(class_cell.count // count):
            for y in range(count):
                result += '*'
            result += '\n'

        for i in range(class_cell % count):
            result += '*'
        return result


my_cell = Cell(16)
print(my_cell + my_cell)
print(my_cell - my_cell)
print(my_cell * my_cell)
print(my_cell / my_cell)
print(my_cell.make_order(my_cell, 6))
