
class Attraction:
  def __init__(self, attraction_name, description):
    self.attraction_name = attraction_name
    self.description = description
    self.animals = list()

  @property
  def last_critter_added(self):
    if len(self.animals) == 0:
      return f"No animals added yet"
    else:
      return self.animals[-1]

  def __str__(self):
    return f"The {self.attraction_name} is {self.description}"

  def add_animal(self, animal_to_add):
    self.animals.append(animal_to_add)
