#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: miorrand <miorrand@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/22 11:03:29 by miorrand            #+#    #+#            #
#   Updated: 2026/04/22 11:03:31 by miorrand           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name.capitalize()
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"Created:{self._name} : {round(self._height, 1)} cm,")
        print(f" {self._age} days old")

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

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def update(self) -> None:
        print(f"Current state: {self._name}: {self._height:.1f} cm,")
        print(f"{self._age} days old\n")


if __name__ == "__main__":
    print(("=== Garden Security System ==="))
    plant1 = Plant("rose", 25, 30)
    plant1.show()
    plant1.set_height(-2)
    plant1.set_age(25)
    plant1.get_height()
    plant1.get_age()
    plant1.update()
