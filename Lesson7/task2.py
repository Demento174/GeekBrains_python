from abc import ABC, abstractmethod
from typing import Union

class ClotheAbstract(ABC):
    __title:str = None
    def __init__(self,title):
        self.__title = title

    @property
    @abstractmethod
    def consumption(self)->float:
        pass

    def __int__(self):
        return int(self.consumption)

    def __float__(self):
        return self.consumption

    def __add__(self, other):

        if isinstance(other,(ClotheAbstract,int)):
            return self.consumption+ int(other)
        else:
            raise TypeError


class Coat(ClotheAbstract):
    V:int = None
    def __init__(self,V:int,title:str):
        self.V = V
        super().__init__(title)

    @property
    def consumption(self)->float:

        return self.V/6.5 + 0.5


class Suit(ClotheAbstract):
    H:int = None

    def __init__(self, H: int, title: str):
        self.H = H
        super().__init__(title)

    @property
    def consumption(self)->float:
        return 2*self.H + 0.3



class Manufactory:
    __clothing_line:list = []



    def __add__(self, other):

        if isinstance(other,ClotheAbstract):
            self.__clothing_line.append(other)
            return self
        else:
            return None

    @property
    def consumption(self) -> float:
        res = 0
        for i in self.__clothing_line:
            res+=float(i)
        # return sum(self.__clothing_line)
        return res

palto = Coat(134,'пальто')
smoking = Suit(234,'Смокинг')

ManufactoryObject = Manufactory()

ManufactoryObject += palto

ManufactoryObject += smoking
print(ManufactoryObject.consumption)