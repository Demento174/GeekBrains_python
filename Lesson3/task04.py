from functools import reduce
def my_func(x, y):
    x= float(x)
    y = int(y)
    if y >=0:
        print('Второе число должно быть отрицательным')
        return None
    # return (x**y)

    res = x
    for i in range(abs(y)-1):
      res*=x

    return 1/res
if __name__ == '__main__':
    print(my_func(*[input(f'{i + 1})Введите число: ') for i in range(2)]))
