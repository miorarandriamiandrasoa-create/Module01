class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name=name.capitalize()
        self.height=height
        self.age=age
    def show(self):
        print(f"{self.name} : {self.height} cm, {self.age} days old")
if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    garden = [
    Plant("rose", 25, 30),
    Plant("sunflower", 80, 45),
    Plant("cactus", 15, 120)
]

for plant in garden:
    plant.show()