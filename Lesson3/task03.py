def my_func(number1: int, number2: int, number3: int) -> int:
    arr = [number1, number2, number3]
    arr.remove(min(arr))
    return sum(arr)


if __name__ == '__main__':
    print(my_func(*[int(input(f'{i + 1})Введите число: ')) for i in range(3)]))
