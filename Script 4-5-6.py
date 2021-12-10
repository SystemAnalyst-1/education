from collections import Counter


class WareHouse:
    items = []

    def __init__(self, area):
        self.area = area

    def add_item(self, item):
        self.items.append(item)

    @property
    def get_count(self):
        count = Counter(self.items)

    def get_item(self, item):
        if self.items.count(item) > 0:
            self.items.remove(item)
            return item
        else:
            return None


class SubOrg(WareHouse):
    items = []

    @staticmethod
    def validate_input(a):
        if not str(a).isdigit():
            return False
        else:
            print("Count should be a number")
            return True

    def take_item(self, item, warehouse, count):
        if SubOrg.validate_input(count):
            while int(count) > 0:
                if warehouse.get_item(item):
                    self.items.append(item)
                count -= 1


class OfficeEquipment:
    def __init__(self, name, power):
        self.name = name
        self.power = power


class Printer(OfficeEquipment):
    def __init__(self, power, name='Printer', color='White'):
        super().__init__(name, power)
        self.color = color


class Scan(OfficeEquipment):
    def __init__(self, power, name='Scan', type=None):
        super().__init__(name, power)
        self.type = type


class Xerox(OfficeEquipment):
    def __init__(self, power, name='Xerox', size=None):
        super().__init__(name, power)
        self.size = size


my_xerox = Xerox(200)
my_warehouse = WareHouse(200)
my_warehouse_2 = SubOrg(100)
my_warehouse.add_item(my_xerox.name)
my_warehouse.add_item(my_xerox.name)
print(my_warehouse.items)
my_warehouse_2.take_item(my_xerox.name, my_warehouse, 2)
my_warehouse_2.take_item(my_xerox.name, my_warehouse, 'a')
print(my_warehouse.items)
print(my_warehouse_2.items)
