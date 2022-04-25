import math


class Square:

    def __init__(self, length: int):
        self._length = length

    def s_square(self):
        s = self._length ** 2
        return s

    def p_square(self):
        p = self._length * 4
        return p

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new_length: int):
        self._length = new_length


class Triangle:

    def __init__(self, height: int, base: int):
        self._height = height
        self._base = base

    def s_triangle(self):
        s = (self._base * self._height) / 2
        return s

    def p_triangle(self):
        p = self._base + (math.sqrt(((self._base / 2) ** 2) + (self._height ** 2)) * 2)
        return p

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height: int):
        self._height = new_height

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, new_base: int):
        self._base = new_base


class Cube(Square):

    def __init__(self, length):
        super().__init__(length)
        self._area = [Square(length), Square(length), Square(length),
                      Square(length), Square(length), Square(length)]

    def area(self):
        i_area = 0
        for i_square in self._area:
            i_area += i_square.s_square()
        return i_area


class Pyramid(Triangle):

    def __init__(self, height, base):
        super().__init__(height, base)
        self._area = [Triangle(height, base), Triangle(height, base),
                      Triangle(height, base), Triangle(height, base),
                      Square(base)]

    def area(self):
        i_area = 0
        for i_figure in self._area:
            try:
                i_area += i_figure.s_triangle()
            except AttributeError:
                i_area += i_figure.s_square()
        return i_area


cube = Cube(5)
print(cube.area())
pyramid = Pyramid(20, 12)
print(pyramid.area())

# зачтено
