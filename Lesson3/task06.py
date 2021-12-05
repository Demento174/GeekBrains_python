int_func = lambda text: text.strip().capitalize()


if __name__ == '__main__':
    [print(int_func(i),end=' ',) for i in input('Введите текст: ').split(' ')]