# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: miorrand <miorrand@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/08 13:58:20 by miorrand          #+#    #+#              #
#    Updated: 2026/04/08 13:58:25 by miorrand         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
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
