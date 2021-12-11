from itertools import count, cycle


def iter_a(start):
    for i in count(start, 1):
        if i > start + 10:
            break
        yield i
    return True


def iter_b(input_list):
    for key, item in enumerate(cycle(input_list)):
        if key >= len(input_list):
            break
        yield item
    return True


if __name__ == '__main__':
    a = iter_a(4)
    print(a.__next__())

    input_list = [1, 5345, 543, 3, 621, 9809]

    b = [i for i in iter_b(input_list)]

    print(b)
