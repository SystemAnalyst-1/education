class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return print("Запуск отрисовки.")


class Pen(Stationery):

    def draw(self):
        return print("Я нарисовала ручкой")


class Pencil(Stationery):

    def draw(self):
        return print("Я нарисовала карандашом")


class Handle(Stationery):

    def draw(self):
        return print("Я нарисовала маркером")


my_class = Stationery("tassel")
my_class.draw()
my_class_1 = Pen("Pen")
my_class_1.draw()
my_class_2 = Pencil("Pencil")
my_class_2.draw()
my_class_3 = Handle("Handle")
my_class_3.draw()
