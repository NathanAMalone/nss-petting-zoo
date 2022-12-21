# from .petting_zoo import PettingZoo
# from .snake_pit import SnakePit
# from .wetlands import Wetlands

# varmint_village = PettingZoo("Varmint Village")
# slither_inn = SnakePit("Slither Inn")
# critter_cove = Wetlands("Critter Cove")

class Attraction:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f'{self.attraction_name} ({len(self)} animals)'

    def __len__(self):
        return len(self.animals)