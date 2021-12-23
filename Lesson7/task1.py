from itertools import zip_longest


class Matrix:
    __list_of_lists: list

    def __init__(self, list_of_lists: list):
        self.__list_of_lists = list_of_lists

    def __str__(self):
        result = ''
        for i in self.__list_of_lists:
            if i != self.__list_of_lists:
                result += '\n'
            for ii in i:
                result += str(ii) + ' '
        return result

    def __add__(self, other):

        matrix = other.__list_of_lists if isinstance(other,Matrix) else other
        return [
                    [self.__list_of_lists[i][j] + matrix[i][j] for j in range(len(self.__list_of_lists[0]))
               ] for i in range(len(matrix))]


matrixObject1 = Matrix([[12, 23, 44], [61, 22, 46], [16, 23, 46]])
matrixObject2 = Matrix([[8, 7, 6], [9, 8, 4], [4, 7, 4]])
r = matrixObject1 + matrixObject2
print(r)
