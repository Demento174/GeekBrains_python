from functools import reduce

if __name__ == '__main__':
    r = [i for i in range(100, 1001) if i % 2 == 0]
    s = reduce(lambda a, b: a * b, r)
    print(s)
