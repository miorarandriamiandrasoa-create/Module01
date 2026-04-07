class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name=name.capitalize()
        self._height=height
        self._age=age
    def show(self):
        print(f"{self._name} : {self._height:.1f} cm, {self._age} days old")
    def grow(self):
        if self._age<35:
            self._height+=0.3
        else:
            self._height+=0.8
    def lifetime(self):
        self._age+=1
    @staticmethod
    def is_year(age) -> bool:
        return age>=365
class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self._color=color
        print("===Flower")
    def show(self):
        super().show()
        print(f" Color: {self._color}")
        print(" Rose has not bloomed yet")
    def bloom(self):
        super().show()
        print(f"{self._name} : {self._height:.1f} cm, {lf._age} days old")
        print(f" Color: {self._color}")
        print(" Rose is blooming beautifully!\n")

class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,trunk_diameter: float):
        super().__init__(name, height, age)
        self._trunk_diameter=trunk_diameter
        print("===Tree")
    def show(self):
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")
    def produce_shade(self):
        print(f"Tree Oak now produces a shade of {self._height:.1f} cm long and {self._trunk_diameter:.1f} cm wide\n")

class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,harvest_season: str, nutritional_value: int):
        super().__init__(name, height, age)
        self._harvest_season=harvest_season.capitalize()
        self._nutritional_value=nutritional_value
        print("===Vegetable")
    def show(self):
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")
    def lifetime(self):
        super().lifetime()
        self._nutritional_value+=1
if __name__ == "__main__":
    print("===Garden statistics===")
    plant2 = Tree("Oak",200,365,5)
    print(f"Is 20 days more than a year? -> {Plant.is_year(20)}")
    print(f"Is 366 days more than a year? -> {Plant.is_year(366)}")
    plant2.show()
    plant2.produce_shade()
 
    
    
