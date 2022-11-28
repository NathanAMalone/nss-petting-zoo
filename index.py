# import the python datetime module to help us create a timestamp
from datetime import date
from .slithering import Snake
from .swimming import Fish, Shark, Eel
from .walking import (Alligator, Camel, Deer, Donkey, Elephant, Fox, Goat,
    Llama, Raccoon, Sheep, Tiger)

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow")
# miss_fuzz.name = "Miss Fuzz"
# miss_fuzz.species = "domestic llama"
miss_fuzz.feed()
miss_fuzz.add_animal()

tigger = Tiger("Tigger", "tiger", "morning", "Tiger Chow")
# tigger.name = "Tigger"
# tigger.species = "tiger"
tigger.feed()
tigger.add_animal()

bitey = Snake("Bitey", "eastern diamondback", "Snake Chow")
# bitey.name = "Bitey"
# bitey.species = "eastern diamondback"
bitey.feed()
bitey.add_animal()

lectric = Eel("Lectric", "electric eel", "Eel Chow")
# lectric.name = "Lectric"
# lectric.species = "electric eel"
lectric.feed()
lectric.add_animal()

bubba = Fish("Bubba", "big mouth bass", "Fish Chow")
# bubba.name = "Bubba"
# bubba.species = "big mouth bass"
bubba.feed()
bubba.add_animal()

leaper = Deer("Leaper", "white tail deer", "morning", "Deer Chow")
# leaper.name = "Leaper"
# leaper.species = "white tail deer"
leaper.feed()
leaper.add_animal()

rocky = Raccoon("Rocky", "raccoon", "morning", "Raccoon Chow")
# rocky.name = "Rocky"
# rocky.species = "raccoon"
rocky.feed()
rocky.add_animal()

basil = Fox("Basil", "red fox", "midday", "Fox Chow")
# basil.name = "Basil"
# basil.species = "red fox"
basil.feed()
basil.add_animal()

trumpy = Elephant("Trumpy", "african elephant", "midday", "Elephant Chow")
# trumpy.name = "Trumpy"
# trumpy.species = "african elephant"
trumpy.feed()
trumpy.add_animal()

jumper = Goat("Jumper", "fainting goat", "midday", "Goat Chow")
# jumper.name = "Jumper"
# jumper.species = "fainting goat"
jumper.feed()
jumper.add_animal()

bray = Donkey("Bray", "american donkey", "midday", "Donkey Chow")
# bray.name = "Bray"
# bray.species = "american donkey"
bray.feed()
bray.add_animal()

humpy = Camel("Humpy", "african camel", "afternoon", "Camel Chow")
# humpy.name = "Humpy"
# humpy.species = "african camel"
humpy.feed()
humpy.add_animal()

hunter = Shark("Hunter", "dwarf lantern shark", "Shark Chow")
# hunter.name = "Hunter"
# hunter.species = "dwarf lantern shark"
hunter.feed()
hunter.add_animal()

dolly = Sheep("Dolly", "asian sheep", "afternoon", "Sheep Chow")
# dolly.name = "Dolly"
# dolly.species = "asian sheep"
dolly.feed()
dolly.add_animal()

chomps = Alligator("Chomps", "american alligator", "afternoon", "Alligator Chow")
# chomps.name = "Chomps"
# chomps.species = "american alligator"
chomps.feed()
chomps.add_animal()