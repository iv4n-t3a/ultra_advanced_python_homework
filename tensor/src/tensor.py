from math import prod


class Tensor:
    def __init__(self, dimension, data):
        if prod(dimension) != len(data):
            raise ValueError('Invalid dimensions')

        self._dimension = dimension
        self._data = data

    @property
    def dimension(self):
        return self._dimension

    @property
    def data(self):
        return self._data

    def __str__(self):
        return str(self._data)


def main():
    t = Tensor((1, 2), [1, 2])
    print(t)


if __name__ == '__main__':
    main()
