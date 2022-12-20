from datetime import date
from attractions import critter_cove
from index import Animal

class Fish(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True
    
    def add_animal(self):
        critter_cove.animals.append(self)

    def __str__(self):
        return f"{self.name} is a {self.species}"