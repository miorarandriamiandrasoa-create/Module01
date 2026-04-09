# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: miorrand <miorrand@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/08 13:58:39 by miorrand          #+#    #+#              #
#    Updated: 2026/04/09 14:09:39 by miorrand         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name} : {self.height:.1f} cm, {self.age} days old")

    def grow(self) -> None:
        if self.age < 35:
            self.height += 0.8
        else:
            self.height += 0.3

    def lifetime(self) -> None:
        self.age += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    plant1 = Plant("rose", 25, 30)
    initial_height = plant1.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant1.show()
        plant1.grow()
        plant1.lifetime()
    print(f"Growth this week: {round(plant1.height - initial_height)}cm")
