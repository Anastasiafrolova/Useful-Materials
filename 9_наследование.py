class SquareMatrix(Matrix):

    def __init__(self, a):
        if isinstance(a, Matrix):
            self.lis = deepcopy(a.lis)
            return
        super().__init__(a)

    def __mul__(self, x):
        return SquareMatrix(super().__mul__(x))
