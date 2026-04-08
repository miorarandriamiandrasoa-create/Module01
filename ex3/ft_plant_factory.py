class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age
        print(
            f"Created:{self.name} : {round(self.height, 1)} cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    garden = [
        Plant("rose", 25, 30),
        Plant("oak", 200, 365),
        Plant("cactus", 5, 90),
        Plant("sunflower", 80, 45),
        Plant("fern", 15, 120)
    ]
