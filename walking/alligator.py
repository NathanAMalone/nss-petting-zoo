from datetime import date
from attractions import varmint_village

class Alligator:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    def add_animal(self):
        varmint_village.animals.append(self)

    def __str__(self):
        return f"{self.name} is a {self.species}"