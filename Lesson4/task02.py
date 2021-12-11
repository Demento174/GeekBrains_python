if __name__ == '__main__':
    input_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

    result = [input_list[key] for key in range(len(input_list)) if key != 0 and (input_list[key] > input_list[key - 1])]
    print(result)
