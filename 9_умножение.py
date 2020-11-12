from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, lst):
        self.lst = deepcopy(lst)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.lst])

    def size(self):
        return len(self.lst), len(self.lst[0])

    def __add__(self, other):
        if self.size() == other.size():
            arr = []
            for row in range(len(self.lst)):
                arr.append([*map(sum, zip(self.lst[row], other.lst[row]))])
            return Matrix(arr)
        else:
            raise MatrixError(self, other)

    def transpose(self):
        self.lst = list(zip(*self.lst))
        return Matrix(self.lst)

    @staticmethod
    def transposed(other):
        return Matrix(list(zip(*other.lst)))

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            arr = []
            for line in self.lst:
                arr.append([*map(lambda x: x * other, line)])
            return Matrix(arr)
        elif isinstance(other, Matrix) and self.size()[1] == other.size()[0]:
            # транспонируем матрицу other, чтобы загнать в zip
            temp = Matrix.transposed(other)
            rows = self.size()[0]
            cols = temp.size()[0]
            # создадим пустой список размером self.rows x other.cols
            arr = [[0 for _ in range(cols)] for _ in range(rows)]
            for row in range(rows):
                for col in range(cols):
                    row_x_col = zip(self.lst[row], temp.lst[col])
                    arr[row][col] = sum(a * b for a, b in row_x_col)
            return Matrix(arr)
        else:
            raise MatrixError(self, other)

    __rmul__ = __mul__


exec(stdin.read())
