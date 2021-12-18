from dataclasses import dataclass


@dataclass
class Car:
    speed:int = None
    color:str = None
    name:str = None
    is_police:bool = None

    def go(self)->None:
        print('Машина поехала')

    def stop(self)->None:
        print('Машина остановилась')

    def turn(self,direction:str)->None:
        print(f'Машина повернула в {direction}')

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.speed}")

class TownCar(Car):

    def __init__(self,speed,color):
        super().__init__(speed,color,'Town car',False)

    def show_speed(self):
        if self.speed>60:
            print("Превыщение скорости")
        super().show_speed()

class SportCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, 'Sport car', False)

class WorkCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, 'Work car', False)

    def show_speed(self):
        if self.speed>40:
            print("Превыщение скорости")
        super().show_speed()

class PoliceCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, 'Police car', True)


def main():
    townCarClass = TownCar(100,'green')
    sportCarClass = TownCar(140, 'yellow')
    workCarClass = TownCar(40, 'red')
    policeCarClass = TownCar(40, 'red')

    sportCarClass.stop()
    sportCarClass.go()
    sportCarClass.turn('лево')

    print(sportCarClass.color)

    townCarClass.show_speed()

if __name__ == '__main__':
    main()
