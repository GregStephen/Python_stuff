from .attraction import Attraction

class PettingZoo(Attraction):
  def __init__(self, attraction_name, description):
    super().__init__(attraction_name, description)    
