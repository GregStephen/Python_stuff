from datetime import date

class Animal:
  def __init__(self, name, species, food, chip_num):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.food = food
    self.__chip_number = chip_num

  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

  @property
  def chip_number(self):
    return self.__chip_number
  
  @chip_number.setter
  def chip_number(self, num):
    pass

  def __str__(self):
    return f"{self.name} is a {self.species}"

