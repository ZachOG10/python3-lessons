class Person:

    def __init__(self, name, age, height, skin_color, race):
        self.name = name
        self.age = age
        self.height = height
        self.skin_color = skin_color
        self.race = race

    def attributes(self):
        return f'{self.name} is a {self.age} year old {self.height} feet tall {self.skin_color} skinned guy from {self.race}.'

zach = Person('Zach',27,6,'light','Africa')
print(f'Name is: {zach.name}')
print(f'age is: {zach.age} years')
print(f'height is: {zach.height} feets tall')
print(f'complexion is: {zach.skin_color} complexion')
print(f'race is: {zach.race}')
print(zach.attributes())

Kator = Person('Kator',22,5.5,'dark','Africa')
print(f'Name is: {Kator.name}')
print(f'age is: {Kator.age} years')
print(f'complexion is: {Kator.skin_color} complexion')
print(f'height is: {Kator.height} feets tall')
print(f'race is: {Kator.race}')
print(Kator.attributes())

## Making an object from a class is called instantiation. 
## A class gives certain objects same attributes. 