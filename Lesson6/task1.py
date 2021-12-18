import time

class incorrectTrafficLightMode(Exception):
    def __init__(self):
        super().__init__('Неверный режим работы светофора')
class TrafficLight:
    __color:str = None

    __green = "\033[32m  green"
    __yellow = "\033[33m  yellow"
    __red = "\033[31m  red"
    __green_time = 4
    __yellow_time = 2
    __red_time = 7


    def running(self):
        self.__switch_traffic_light(self.__red,self.__red_time)

        self.__switch_traffic_light(self.__yellow, self.__yellow_time)

        self.__switch_traffic_light(self.__green, self.__green_time)


    def __switch_traffic_light(self,color,durationWork):
        self.__color = color
        print(self.__color)
        time.sleep(durationWork)





def main():
    trafficLightClass = TrafficLight()
    trafficLightClass.running()


if __name__ == '__main__':
    main()