from datetime import date

class Snake:

    def __init__(self, name, species):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True