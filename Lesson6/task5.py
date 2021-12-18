from dataclasses import dataclass


@dataclass
class Stationery:
    title:str = None

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):

    def __init__(self):

        super().__init__('Ручка')

    def draw(self):
        print("Запуск отрисовки Карандошом")


class Pencil(Stationery):
    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        print("Запуск отрисовки ручкой")

class Handle(Stationery):
    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        print("Запуск отрисовки маркером")

def main():
    penClass = Pen()
    pencilClass = Pencil()
    handlerClass = Handle()
    penClass.draw()
    pencilClass.draw()
    handlerClass.draw()


if __name__ == '__main__':
    main()
