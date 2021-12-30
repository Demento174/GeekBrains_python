"""
1.Реализовать класс «Дата», функция-конструктор которого должна
 принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с
декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class InvalidDayError(Exception):
    pass


class InvalidMonthError(Exception):
    pass


class Data:
    day: int
    month: int
    year: int

    def __init__(self, date: str):
        date = self.convert_to_number(date)
        self.day = date[0]
        self.month = date[1]
        self.year = date[2]

    @classmethod
    def convert_to_number(cls, date):
        return [int(i) for i in date.split('-')]

    @staticmethod
    def validate(day, month):

        if 1 > day or day > 31:
            raise InvalidDayError
        if 1 > month or month > 12:
            raise InvalidMonthError


data = Data('2-51-2008')

Data.validate(data.day, data.month)
