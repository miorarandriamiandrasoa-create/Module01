class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name=name.capitalize()
        self.height=height
        self.age=age
        print(f"Created:{self.name} : {self.height:.1f} cm, {self.age} days old")
if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    garden = [
        Plant("rose",25, 30),
        Plant("oak",200, 365),
        Plant("cactus",5, 90),
        Plant("sunflower",80, 45),
        Plant("fern",15, 120)
    ]