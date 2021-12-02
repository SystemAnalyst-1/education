class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_road(self, weight_m, height):
        if type(weight_m) == int and type(height) == int and type(self._length) == int and type(self._width) == int:
            weight = self._width * self._length * weight_m * height
            return f'{self._width}м * {self._length}м * {weight_m}кг * {height}см = {weight} т'
        else:
            return "Вы ввели не число"


my_road_1 = Road(5, 10)
print(my_road_1.weight_road(2, 2))
