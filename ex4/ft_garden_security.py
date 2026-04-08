class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name.capitalize()
        self._height = height
        self._age = age

    def show(self) -> None:
        print(
            f"Plant created: {self._name}: {self._height:.1f} cm, {self._age} days old\n")

    def set_height(self, height: int) -> None:
        if (height < 0):
            print(
                f"{self._name} :Error, height can't be negative\nHeight update rejected")
        else:
            self._height = height
            print(f"Height updated:{self._height}cm\n")

    def set_age(self, age:int) -> None:
        if (age < 0):
            print(f"{self._name} :Error, age can't be negative\nAge update rejected")
        else:
            self._age = age
            print(f"Age updated:{self._age}days\n")

    def get_height(self) ->int:
        return self._height

    def get_age(self) ->int:
        return self._age

    def update(self) -> None:
        print(
            f"Current state: {self._name}: {self._height:.1f} cm, {self._age} days old\n")


if __name__ == "__main__":
    print(("=== Garden Security System ==="))
    plant1 = Plant("rose", 25, 30)
    plant1.show()
    plant1.set_height(-2)
    plant1.set_age(25)
    plant1.get_height()
    plant1.get_age()
    plant1.update()
