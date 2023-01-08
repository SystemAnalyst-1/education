class Worker:

    def __init__(self, name, surname, position, wage=0, bonus=0):
        income = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(f'Моё полное имя {self.name} {self.surname}')
        return

    def get_total_income(self):
        print(sum(self._income.values()))
        return 


my_position = Position("Artem", "Lomakin", "Developer", 100)
my_position_2 = Position("Artem", "Lomakin", "Developer", 100, 10)
my_position_3 = Position("Artem", "Lomakin", "Developer")

my_position.get_full_name()
my_position.get_total_income()
my_position_2.get_full_name()
my_position_2.get_total_income()
my_position_3.get_full_name()
my_position_3.get_total_income()