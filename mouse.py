class Mouse:
    def __init__(self, width, height, color, belly, x, y):
        self._width = width
        self._height = height
        self._color = color
        self._belly = belly
        self._x = x
        self._y = y

    # Getter and Setter for width
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    # Getter and Setter for height
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    # Getter and Setter for color
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    # Getter and Setter for belly
    @property
    def belly(self):
        return self._belly

    @belly.setter
    def belly(self, value):
        self._belly = value

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

