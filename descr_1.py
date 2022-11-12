class NonNegative:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    _lengt = NonNegative()
    _width = NonNegative()

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        self.weigth = 25
        self.tickness = 0.05
        mass = self._length * self._width * self.weigth * self.tickness / 1000
        #print(f'Need {mass} ton for the building')
        return mass


OBJ = Road(5000, 20)
print(OBJ.mass())

OBJ._lengt = 5000
OBJ._width = -20
print(OBJ.mass())

OBJ._lengt = 5000
OBJ._width = 20
print(OBJ.mass())
