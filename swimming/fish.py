from datetime import date

class Fish:

    def __init__(self, name, species):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True