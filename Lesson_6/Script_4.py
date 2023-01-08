class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, spd=10):
        self.speed += spd
        print("Я ускорилась на 10")
        return

    def stop(self):
        self.speed = 0
        print("Я остановилась")
        return

    def turn(self, direction):
        return print(f'Я повернула на {direction}')

    def show_speed(self):
        return print(f'Моя скорость {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return print(f'Вы превысили скорость на {self.speed - 60}')
        else:
            return print(f'Моя скорость {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print(f'Вы превысили скорость на {self.speed - 40}')
        else:
            return print(f'Моя скорость {self.speed}')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


class SportCar(Car):

    def __init__(self, speed, name, color="Red", is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


my_car = Car(10, 'Volvo', 'Green')
my_car.turn('Left')
my_car.stop()
my_car.go(100)
my_car.show_speed()

my_car = TownCar(10, 'Volvo', 'Green')
my_car.turn('Left')
my_car.stop()
my_car.go(100)
my_car.show_speed()

my_car = PoliceCar(10, 'Volvo', 'Green')
my_car.turn('Left')
my_car.stop()
my_car.go(100)
my_car.show_speed()
print(my_car.is_police)

my_car = WorkCar(10, 'Volvo', 'Green')
my_car.turn('Left')
my_car.show_speed()
my_car.stop()
my_car.go(100)
my_car.show_speed()

my_car = SportCar(10, 'Volvo')
my_car.turn('Left')
my_car.stop()
my_car.go(100)
my_car.show_speed()
print(my_car.color)
