from animals import Goat, Goose, Llama, Shark, Pig, Snake
from attractions import PettingZoo

bob = Goose("Bob", "Canada goose", "watercress sandwiches", 243234)
bob.run()
bob.swim()

snappy = Shark("Snappy", "Great White", "Fingers", 2342352)

varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scurry")
varmint_village.add_animal(bob)
varmint_village.add_animal(snappy)
print(varmint_village)
for animal in varmint_village.animals:
  print(animal)