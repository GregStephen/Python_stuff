from .attraction import Attraction

class PettingZoo(Attraction):
    def __init__(self, attraction_name, description):
        super().__init__(attraction_name, description)

    def add_animal(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(
                f'{animal} doesn\'t like to be petted, so please do not put it in the {self.attraction_name} attraction.')
