"""
5. Продолжить работу над первым заданием. Разработать методы,
отвечающие за приём оргтехники на склад и передачу в определенное
подразделение компании. Для хранения данных о наименовании и количестве
единиц оргтехники, а также других данных, можно использовать любую подходящую
структуру, например словарь.
"""
from abc import ABC
from typing import Union


class OfficeEquipment:
    name: str
    price: int

    def __init__(self, name, price):
        self.name = name
        self.price = price


class DataProducts(ABC):
    printers: dict
    xerox: dict
    scanners: dict



    def __init__(self):
        self.printers = {'items':[],'count': 0, 'total_price': 0}
        self.xerox = {'items':[],'count': 0, 'total_price': 0}
        self.scanners = {'items':[],'count': 0, 'total_price': 0}

    def _sum_product(self, productsList: dict, product: Union[OfficeEquipment,dict], count: int):
        productsList['count'] += count
        productsList['total_price'] += product.price * count
        productsList['items'].append(product)
        return productsList

    def add_product(self, product, count=1):
        if isinstance(product, Printer):
            self.printers = self._sum_product(self.printers, product, count)
        elif isinstance(product, Xerox):
            self.xerox = self._sum_product(self.xerox, product, count)
        else:
            self.scanners = self._sum_product(self.scanners, product, count)


class SubdivisionsOfTheCompanyParent(DataProducts):
    pass


class SubdivisionsOfTheCompanyOne(SubdivisionsOfTheCompanyParent):
    pass


class SubdivisionsOfTheCompanyTwo(SubdivisionsOfTheCompanyParent):
    pass




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


class Warehouse(DataProducts):
    products = []

    def add_product(self, product, count=1):
        self.products.append(product)
        super(Warehouse, self).add_product(product, count)

    def sort(self):
        subDivisionA = SubdivisionsOfTheCompanyOne()
        subDivisionB = SubdivisionsOfTheCompanyTwo()


        subDivisionA.add_product(self.printers['items'][0])
        subDivisionA.add_product(self.printers['items'][1])

        subDivisionB.add_product(self.xerox['items'][0])
        subDivisionB.add_product(self.scanners['items'][0])

        print(subDivisionA.__dict__)
        print(subDivisionB.__dict__)


printerObject = Printer('Printer', 100, 'color')
printerObject1 = Printer('Printer1', 160, 'color')

xeroxObject = Xerox('Xerox', 4324, 34)

scannerObject = Scanner('Scanner', 234, 100)

warehouseObject = Warehouse()

warehouseObject.add_product(printerObject, 2)
warehouseObject.add_product(printerObject1, 2)
warehouseObject.add_product(xeroxObject,34)
warehouseObject.add_product(scannerObject,25)
warehouseObject.sort()
