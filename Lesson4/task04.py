def generate_list(input_list: list):
    for i in input_list:
        if input_list.count(i) == 1:
            yield i
        continue
    return True


if __name__ == '__main__':
    input_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result = [i for i in generate_list(input_list)]
    print(result)
