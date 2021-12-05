def my_func():
    i = 0
    while True:
        arr = input('Вводите числа через пробел, для прекрашения введите любой символ не типа int: ').split(' ')
        for x in arr:
            if x == '':
                continue
            try:
                i += int(x)
            except ValueError:
                return i

        print(i)










if __name__=='__main__':
    print(my_func())