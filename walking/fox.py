from datetime import date
from attractions import varmint_village
from index import Animal

class Fox(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)        
        self.walking = True
        self.shift = shift

    def add_animal(self):
        varmint_village.animals.append(self)

    def __str__(self):
        return f"{self.name} is a {self.species}"