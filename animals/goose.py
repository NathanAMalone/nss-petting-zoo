# The package syntax is what allows for these clean import statements
from .animal import Animal
from movements import Walking, Swimming
from index import critter_cove

class Goose(Animal, Walking, Swimming):

    def __init__(self, name, species, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
        # no more self.swimming = True
        ...

    def honk(self):
        print("The goose honks. A lot")

    def run(self):
        print(f'{self} waddles.')

    def add_animal(self):
        critter_cove.animals.append(self)

    def __str__(self):
        return f'{self.name} the Goose'