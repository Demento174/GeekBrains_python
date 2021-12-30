"""
2. Создайте собственный класс-исключение, обрабатывающий
ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""


class CustomZeroError(Exception):
    def __str__(self):
        return 'My custom exception error'


def func():
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))

    if b == 0:
        raise CustomZeroError
    return a / b


if __name__ == '__main__':
    try:
        print(func())

    except CustomZeroError:
        print('Вообще делить на ноль можно, в этом случаи результат будет бесконечность')
