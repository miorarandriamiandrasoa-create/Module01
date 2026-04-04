class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name=name.capitalize()
        self.height=height
        self.age=age
    def show(self):
        print(f"{self.name} : {self.height:.1f} cm, {self.age} days old")
    def grow(self):
        if self.age<35:
            self.height+=0.3
        else:
            self.height+=0.8
    def lifetime(self):
        self.age+=1
if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    plant1 = Plant("rose",25, 30)
    initial_height = plant1.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant1.show()
        plant1.grow()
        plant1.lifetime()
    print(f"Growth this week: {round(plant1.height - initial_height)}cm")