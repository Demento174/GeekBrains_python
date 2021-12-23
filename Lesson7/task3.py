def decorate_check_instance_cage(func):
    def wrapper(*args,**kwargs):
        if isinstance(args[1],Cage):
            return func(*args, **kwargs)
        else:
            raise TypeError

    return wrapper

class Cage:
    __cellCount:int = None

    def __init__(self,cellCount:int)->None:
        self.__cellCount = cellCount

    def make_over(self,part_size):
        result =''
        for i in range(1,self.__cellCount+1):
            result+=' * '
            if i%part_size == 0:
                result+='\n'
        return result

    @property
    def cellCount(self):
        return self.__cellCount

    @decorate_check_instance_cage
    def __add__(self,other):
        return Cage(other.cellCount + self.cellCount)

    @decorate_check_instance_cage
    def __sub__(self,other):
        result = self.cellCount - other.cellCount
        if result < 0:
            raise ValueError('Количетсов ячеек не может быть меньше 0')
        return Cage(result)

    @decorate_check_instance_cage
    def __mul__(self,other):
        return Cage(self.cellCount * other.cellCount)

    @decorate_check_instance_cage
    def __truediv__(self,other):
        return Cage(self.cellCount // other.cellCount)


Cage1 = Cage(13)
Cage2 = Cage(132)

sum = Cage1+Cage2
minus = Cage2-Cage1
multiple = Cage1*Cage2
delenie = Cage2/Cage1
print(Cage1.make_over(3))