"""
7.Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число», реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplexNumbers:
    a:int
    b:int
    def __init__(self,a,b):
        self.a =a
        self.b = b

    def __add__(self, other):
        return f"{self.a + other.a}+{self.b + other.b}i"

    def __mul__(self, other):
        return f"{self.a*other.a - self.b*other.b}+{self.a*other.b + self.b*other.a}i"

    def __str__(self):
        return f"{self.a} + {self.b}i"




number_1 = ComplexNumbers(5,7)
number_2 = ComplexNumbers(9,6)

if(number_1+number_2!='14+13i'):
    raise Exception(f'Метод сложения работает не корректно, ожидалось: 14+13i , а получили {number_1+number_2}')
if(number_1*number_2 !="3+93i"):
    raise Exception(f'Метод умножения работает не корректно, ожидалось: 3+93i , а получили {number_1*number_2}')