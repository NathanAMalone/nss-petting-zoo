from datetime import date
from index import varmint_village
from .animal import Animal

class Elephant(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)        
        self.walking = True
        self.shift = shift

    def add_animal(self):
        varmint_village.animals.append(self)

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed bales of {self.food} on {date.today().strftime("%m/%d/%Y")}')