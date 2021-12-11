from itertools import count
from functools import reduce
def my_favorite_generate(n):
    for i in count(1):
        if i>n:
            break
        arr= [ii+1 for ii in range(i)]
        yield reduce(lambda a,b:a*b,arr)

if __name__=='__main__':
    n = 5
    [print(el) for el in my_favorite_generate(n)]

        # pass