class NonNegativeInt:

    def __set__(self, instance, value):
        if isinstance(value, int):
            instance.__dict__[self.my_attr] = value
        else:
            raise TypeError("Может быть только целым числом")

        if value < 0:
            raise ValueError("Не может быть отрицательным")

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    wage = NonNegativeInt()
    bonus = NonNegativeInt()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


OBJ = Position('Сергей', 'Иванов', 'Инженер', 100000, 25000)
print(OBJ.get_total_income())

OBJ.wage = -100000
OBJ.bonus = 25000
print(OBJ.get_total_income())

OBJ.wage = 100000
OBJ.bonus = 25000.5
print(OBJ.get_total_income())

OBJ.wage = 100000
OBJ.bonus = 25000
print(OBJ.get_total_income())
