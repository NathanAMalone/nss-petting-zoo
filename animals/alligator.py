from index import varmint_village
from .animal import Animal
from movements import Walking, Swimming

class Alligator(Animal, Walking, Swimming):

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        Swimming.__init__(self)
        self.shift = shift

    
    def add_animal(self):
        varmint_village.animals.append(self)

    def __str__(self):
        return f"{self.name} is a {self.species}"

    @property
    def chip_number(self):
        return self.__chip_number
    
    @chip_number.setter
    def chip_number(self, number):
        pass

    