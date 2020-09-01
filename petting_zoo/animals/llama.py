from .animal import Animal

class Llama(Animal):
  def __init__(self, name, species, shift, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.shift = shift
    self.walking = True

  def feed(self):
    print(f'on {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')