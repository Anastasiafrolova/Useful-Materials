from sys import stdin
import copy


class Matrix:
    def __init__(self, e):
        self.e = copy.deepcopy(e)

    def __str__(self):
        self.res = ""
        ii = 0
        for i in self.e:
            self.res += '\t'.join(map(str, i))
            ii += 1
            if ii < len(self.e):
                self.res += '\n'
        return self.res

    def size(self):
        return len(self.e), len(self.e[0])


exec(stdin.read())
