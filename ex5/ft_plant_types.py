class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name=name.capitalize()
        self._height=height
        self._age=age
    def show(self):
        print(f"Plant created: {self._name}: {self._height:.1f} cm, {self._age} days old\n")
class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color=color
    def bloom(self):

class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter=trunk_diameter
    def produce_shade(self):

class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,harvest_season: str, nutritional_value: int):
        super().__init__(name, height, age)
        self.harvest_season=harvest_season
        self.nutritional_value=nutritional_value
if __name__ == "__main__":