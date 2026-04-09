# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_intro.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: miorrand <miorrand@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/08 13:58:05 by miorrand          #+#    #+#              #
#    Updated: 2026/04/08 13:58:29 by miorrand         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_garden_intro(name: str, height: int, age: int) -> None:
    print("=== Welcome to My Garden ===")
    print(f"Plant:{name.capitalize()}")
    print(f"Height:{height} cm")
    print(f"Age:{age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro("tulip", 15, 10)
