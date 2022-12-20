from datetime import date
from attractions import slither_inn
from index import Animal

class Snake(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
    
    def add_animal(self):
        slither_inn.animals.append(self)
    
    def __str__(self):
        return f"{self.name} is a {self.species}"