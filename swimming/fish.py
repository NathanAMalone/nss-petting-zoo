from datetime import date
from attractions import critter_cove

class Fish:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    def add_animal(self):
        critter_cove.animals.append(self)

    def __str__(self):
        return f"{self.name} is a {self.species}"