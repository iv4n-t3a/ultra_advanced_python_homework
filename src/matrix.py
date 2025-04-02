from tensor import Tensor

import builtins
import itertools


class Matrix(Tensor):
    def __init__(self, dimension, data):
        if len(dimension) != 2:
            raise ValueError(f'{type(self).__name__} is 2d tensor')
        super().__init__(dimension, data)

    def conv_rc2i(self, r, c):
        return c + self.dimension[0] * r

    def conv_i2rc(self, i):
        return divmod(i, self.dimension[0])

    def __str__(self):
        elemsize = max(len(str(i)) for i in self.data)
        rightelemsize = max(len(str(j)) if i %
                            self.dimension[0] == 0 else 0 for i, j in enumerate(self.data))
        res = '[\n'

        for i, j in enumerate(self.data):
            if i % self.dimension[0] == 0:
                res += '    ' + (rightelemsize - len(str(j))
                                 ) * ' ' + str(j) + ', '
            elif i % self.dimension[0] == self.dimension[0] - 1:
                res += (elemsize - len(str(j))) * ' ' + str(j) + '\n\n'
            else:
                res += (elemsize - len(str(j))) * ' ' + str(j) + ', '

        return res[:-1] + ']'

    def __eq__(self, other):
        return self.dimension == other.dimension and self.data == other.data

    def __getitem__(self, key):
        match type(key):
            case builtins.int:
                idx = Matrix.__getIntIndex(key, self.dimension[1])
                return self.data[idx * self.dimension[0]: (idx + 1) * self.dimension[0]]

            case builtins.list:
                return list(itertools.chain.from_iterable(self[i] for i in key))

            case builtins.tuple:
                if len(key) != 2:
                    raise IndexError('Matrix is 2d tensor')
                row, col = key

                rowIndecies = Matrix.__getIndeces(row, self.dimension[0])
                colIndecies = Matrix.__getIndeces(col, self.dimension[1])

                items = [self.__getItem(r, c)
                         for r in rowIndecies for c in colIndecies]
                return Matrix.__itemsToMatrix(items)

            case builtins.slice:
                items = [self[i] for i in range(*key.indices(self.dimension[0]))]
                return Matrix.__itemsToMatrix(items)

            case _:
                raise IndexError(f'Unsupported index type {
                                 type(key).__name__}')

    def __getItem(self, row: int, col: int):
        row = Matrix.__getIntIndex(row, self.dimension[0])
        col = Matrix.__getIntIndex(col, self.dimension[1])
        return self.data[self.conv_rc2i(row, col)]

    @staticmethod
    def __itemsToMatrix(items):
        if len(items) == 1:
            return items[0]
        return Matrix((len(items[0]), len(items)), [num for row in items for num in row])

    @staticmethod
    def __getIndeces(key, size):
        match type(key):
            case builtins.int:
                return [Matrix.__getIntIndex(key, size)]
            case builtins.list:
                return key
            case builtins.tuple:
                return key
            case builtins.slice:
                return (i for i in range(*key.indices(size)))
            case _:
                raise IndexError(f'Unsupported index type {
                                 type(key).__name__}')

    @staticmethod
    def __getIntIndex(index, size):
        if index <= -size or index >= size:
            raise IndexError('Matrix index out of range')
        return index % size
