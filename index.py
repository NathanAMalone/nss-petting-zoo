# import the python datetime module to help us create a timestamp
from animals import (Alligator, Camel, Deer, Donkey, Eel, Elephant, Fish,
    Fox, Goat, Goose, Llama, Raccoon, Shark, Sheep, Snake, Tiger)
from attractions import PettingZoo, SnakePit, Wetlands


varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scurry")
critter_cove = Wetlands("Critter Cove", "marshiness magic")
slither_inn = SnakePit("Slither Inn", "slithery surprises in every corner")

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow", 546258)
# miss_fuzz.name = "Miss Fuzz"
# miss_fuzz.species = "domestic llama"
miss_fuzz.feed()
miss_fuzz.add_animal()
varmint_village.add_animal_pythonic(miss_fuzz)
varmint_village.add_animal_type_check(miss_fuzz)

tigger = Tiger("Tigger", "tiger", "morning", "Tiger Chow", 465463)
# tigger.name = "Tigger"
# tigger.species = "tiger"
tigger.feed()
tigger.add_animal()

bitey = Snake("Bitey", "eastern diamondback", "Snake Chow", 56987658)
# bitey.name = "Bitey"
# bitey.species = "eastern diamondback"
bitey.feed()
bitey.add_animal()

lectric = Eel("Lectric", "electric eel", "Eel Chow", 456486524)
# lectric.name = "Lectric"
# lectric.species = "electric eel"
lectric.feed()
lectric.add_animal()
varmint_village.add_animal_pythonic(lectric)

bubba = Fish("Bubba", "big mouth bass", "Fish Chow", 987632)
# bubba.name = "Bubba"
# bubba.species = "big mouth bass"
bubba.feed()
bubba.add_animal()

leaper = Deer("Leaper", "white tail deer", "morning", "Deer Chow", 452318)
# leaper.name = "Leaper"
# leaper.species = "white tail deer"
leaper.feed()
leaper.add_animal()

rocky = Raccoon("Rocky", "raccoon", "morning", "Raccoon Chow", 7531258)
# rocky.name = "Rocky"
# rocky.species = "raccoon"
rocky.feed()
rocky.add_animal()

basil = Fox("Basil", "red fox", "midday", "Fox Chow", 65387532)
# basil.name = "Basil"
# basil.species = "red fox"
basil.feed()
basil.add_animal()

trumpy = Elephant("Trumpy", "african elephant", "midday", "Elephant Chow", 34567)
# trumpy.name = "Trumpy"
# trumpy.species = "african elephant"
trumpy.feed()
trumpy.add_animal()

jumper = Goat("Jumper", "fainting goat", "midday", "Goat Chow", 85234563)
# jumper.name = "Jumper"
# jumper.species = "fainting goat"
jumper.feed()
jumper.add_animal()

bray = Donkey("Bray", "american donkey", "midday", "Donkey Chow", 12354753)
# bray.name = "Bray"
# bray.species = "american donkey"
bray.feed()
bray.add_animal()

humpy = Camel("Humpy", "african camel", "afternoon", "Camel Chow", 32488635)
# humpy.name = "Humpy"
# humpy.species = "african camel"
humpy.feed()
humpy.add_animal()

hunter = Shark("Hunter", "dwarf lantern shark", "Shark Chow", 95575347)
# hunter.name = "Hunter"
# hunter.species = "dwarf lantern shark"
hunter.feed()
hunter.add_animal()

dolly = Sheep("Dolly", "asian sheep", "afternoon", "Sheep Chow", 1422553)
# dolly.name = "Dolly"
# dolly.species = "asian sheep"
dolly.feed()
dolly.add_animal()

chomps = Alligator("Chomps", "american alligator", "afternoon", "Alligator Chow", 2221112)
# chomps.name = "Chomps"
# chomps.species = "american alligator"
chomps.run()
chomps.swim()
chomps.feed()
chomps.add_animal()

bob = Goose("Bob", "Canada goose", "watercress sandwiches", 6547564)
bob.run()
bob.swim()

varmint_village.add_animal(bob)

for animal in varmint_village.animals:
    print(animal)

