#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: miorrand <miorrand@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/22 11:03:54 by miorrand            #+#    #+#            #
#   Updated: 2026/04/22 11:03:55 by miorrand           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:
    class stat:
        def __init__(self) -> None:
            self._grow = 0
            self._show = 0
            self._lifetime = 0
            self._produce_shade = 0

        def stat_grow(self) -> None:
            self._grow += 1

        def stat_show(self) -> None:
            self._show += 1

        def stat_lifetime(self) -> None:
            self._lifetime += 1

        def stat_shade(self) -> None:
            self._produce_shade += 1

        def get_grow(self) -> int:
            return (self._grow)

        def get_show(self) -> int:
            return (self._show)

        def get_lifetime(self) -> int:
            return (self._lifetime)

        def get_shade(self) -> int:
            return (self._produce_shade)

    def get_stats(self) -> tuple[int, int, int]:
        return (self._stat.get_grow(),
                self._stat.get_show(),
                self._stat.get_lifetime())

    def get_shade(self) -> int:
        return (self._stat.get_shade())

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        self._height = round(height, 1)
        self._age = age
        self._stat = Plant.stat()

    @staticmethod
    def is_year(age: int) -> bool:
        if age < 366:
            return False
        else:
            return True

    @classmethod
    def anonymous(cls) -> "Plant":
        print("\n=== Anonymous")
        return cls("Unknnown plant", 00.0, 0)

    def set_height(self, height: int) -> None:
        if (height < 0):
            print(f"{self._name} :Error, height can't be negative\n")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated:{self._height}cm\n")

    def set_age(self, age: int) -> None:
        if (age < 0):
            print(f"{self._name} :Error, age can't be negative\n")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated:{self._age}days\n")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name} : {self._height:.1f} cm, {self._age} days old")
        self._stat.stat_show()

    def grow(self) -> None:
        if self._age < 35:
            self._height += 8
        else:
            self._height += 1.5
        self._stat.stat_grow()

    def lifetime(self) -> None:
        self._age += 1
        self._stat.stat_lifetime()


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, color: str, header: bool = True) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._blooming = False
        if header:
            print("\n=== Flower")

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._blooming is False:
            print(" Rose has not bloomed yet")
        else:
            print(" Rose is blooming beautifully!")

    def bloom(self) -> None:
        self._blooming = True


class Seed(Flower):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age, color, header=False)
        self._seed = 0
        print("\n=== Seed")

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seed}")

    def bloom(self) -> None:
        super().bloom()
        self._seed += 42


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = float(trunk_diameter)
        self._shade = False
        print("\n===Tree")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        print(f"Tree Oak now produces a shade of {self._height}", end="")
        print(f" cm long and {self._trunk_diameter:.1f} cm wide")
        self._stat.stat_shade()


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


def print_stat(plant: Plant) -> None:
    grow, show, lifetime = plant.get_stats()
    print(f"Stats: {grow} grow, {lifetime} age, {show} show")
    if isinstance(plant, Tree):
        print(f"  {plant.get_shade()} shade")


if __name__ == "__main__":
    print("===Garden Plant Types===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_year(400)}")
    rose = Flower("rose", 15, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    print_stat(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    print_stat(rose)
    oak = Tree("oak", 200, 365, 5)
    oak.show()
    print("[statistics for Oak]")
    print_stat(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    print_stat(oak)
    sunflower = Seed("sunflower", 80, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    for i in range(0, 20):
        sunflower.grow()
        sunflower.lifetime()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    print_stat(sunflower)
    plant = Plant.anonymous()
    plant.show()
    print_stat(plant)
