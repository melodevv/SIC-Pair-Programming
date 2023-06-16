class Cat:
    # Cat_labor_months = 3          # Class Variable

    # Constructor
    def __init__(self, name, color, age):
        self.__name = name            # Instance Variable
        self.__color = color          # Instance Variable
        self.__age = age

    def meow(self):
        print('My name is {}, color is {}, meow meow~~' .format(self.__name, self.__color))

    def set_age(self, age):
        if age > 0:
            self.__age = age

    def get_age(self):
        return self.__age

    # This is similar to ToString() method in C#
    def __str__(self):
        return 'Cat(name=' + self.__name + ', Color=' + self.__color + ')'


nabi = Cat('nabi', 'black', 4)
nero = Cat('nero', 'white', 5)

#
# Trigger the __str__ special method
#
print(nabi)
print(nero)
print()

#
# Class the Meow() method
nabi.meow()
nero.meow()
