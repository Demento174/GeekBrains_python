"""
4.Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс
«Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа
оргтехники.
"""


class OfficeEquipment:
    name: str
    price: int

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Warehouse:
    products: list
    total_price: int

    def __init__(self):
        self.products = []
        self.total_price = 0

    def add_product(self, product: OfficeEquipment):
        self.products.append(product)
        self.total_price += product.price


class Printer(OfficeEquipment):
    color = ['color', 'black_and_white']

    def __init__(self, name, price, color):
        self.color = color
        super().__init__(name, price)


class Xerox(OfficeEquipment):
    speed: int

    def __init__(self, name, price, speed):
        self.speed = speed
        super().__init__(name, price)


class Scanner(OfficeEquipment):
    dpi: int

    def __init__(self, name, price, dpi):
        self.dpi = dpi
        super().__init__(name, price)


printerObject = Printer('Printer', 100, 'color')

xeroxObject = Xerox('Xerox', 4324, 34)

scannerObject = Scanner('Scanner', 234, 100)

warehouseObject = Warehouse()

warehouseObject.add_product(printerObject)
warehouseObject.add_product(xeroxObject)
warehouseObject.add_product(scannerObject)
print(warehouseObject.total_price)
