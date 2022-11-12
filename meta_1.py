class SingletonMeta(type):
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)

        return cls.instance


class MyClass(metaclass=SingletonMeta):
    def __init__(self, length, width):
        self.length = length
        self.width = width
     

OBJ_1 = MyClass(10,20)
OBJ_2 = MyClass()
OBJ_3 = MyClass()
OBJ_4 = MyClass()

print(OBJ_1 == OBJ_2)
print(OBJ_2 == OBJ_3)
print(OBJ_3 == OBJ_4)
