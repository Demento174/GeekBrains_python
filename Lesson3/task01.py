def division(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 'При делении на ноль получается бессконечность'



if __name__ == '__main__':
    print(division(*[int(input(f'{i+1})Введите число: ')) for i in range(2)]))