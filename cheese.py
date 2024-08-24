class Cheese:
    def __init__(self, size, color, x, y):
        self._size = size
        self._color = color
        self._x = x
        self._y = y

    # Getter and Setter for size
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    # Getter and Setter for color
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    # Getter and Setter for x
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    # Getter and Setter for y
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

