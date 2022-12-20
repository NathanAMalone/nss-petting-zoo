class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

    def __str__(self):
        for animal in self.animals:
            return (f"{self.attraction_name} is where you'll find {self.description}, like"
                f"{animal.name} the {animal.species}")
    
    @property
    def last_critter_added(self):
        return self.animals[-1]