# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: miorrand <miorrand@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/08 13:59:24 by miorrand          #+#    #+#              #
#    Updated: 2026/04/09 14:29:28 by miorrand         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        self._height = height
        self._age = age

    def set_height(self, height: int) -> None:
        if (height < 0):
            print(
                f"{self._name} :Error, height can't be negative\nHeight update rejected")
        else:
            self._height = height
            print(f"Height updated:{self._height}cm\n")

    def set_age(self, age: int) -> None:
        if (age < 0):
            print(f"{self._name} :Error, age can't be negative\nAge update rejected")
        else:
            self._age = age
            print(f"Age updated:{self._age}days\n")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name} : {self._height:.1f} cm, {self._age} days old")

    def grow(self) -> None:
        if self._age < 35:
            self._height += 0.3
        else:
            self._height += 0.8

    def lifetime(self) -> None:
        self._age += 1


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._blooming = False
        print("===Flower")

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._blooming is False:
            print(" Rose has not bloomed yet")
        else:
            print(" Rose is blooming beautifully!\n")

    def bloom(self) -> None:
        self._blooming = True


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = float(trunk_diameter)
        self._shade = False
        print("===Tree")

    def show(self) -> None:
        super().show()
        if self._shade is False:
            print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")
        else:
            print(f"Tree Oak now produces a shade of {self._height}", end="")
            print(f" cm long and {self._trunk_diameter:.1f} cm wide\n")

    def produce_shade(self) -> None:
        self._shade = True


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season.capitalize()
        self._nutritional_value = nutritional_value
        print("===Vegetable")

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def lifetime(self) -> None:
        super().lifetime()
        self._nutritional_value += 1


if __name__ == "__main__":
    print("===Garden Plant Types===")
    plant1 = Tree("oak", 200, 365, 5)
    plant1.show()
    plant1.produce_shade()
    plant1.show()
