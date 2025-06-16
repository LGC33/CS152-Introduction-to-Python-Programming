"""Utility to convert quarts into barrels and ounces."""

# Author: Larry Grace

# Algorithm
# 1. Prompt the user for the number of quarts.
# 2. Compute how many whole barrels that represents.
# 3. Determine the remaining quarts that do not make a full barrel.
# 4. Convert the total quarts to ounces.
# 5. Display the results.

QUARTS_PER_BARREL = 168
OUNCES_PER_QUART = 32

def main() -> None:
    total_quarts = int(input("Enter a positive number of quarts: "))
    barrels = total_quarts // QUARTS_PER_BARREL
    remaining_quarts = total_quarts % QUARTS_PER_BARREL
    total_ounces = total_quarts * OUNCES_PER_QUART

    print(f"\nYou entered {total_quarts} quarts, which is:")
    print(f"{barrels} barrels and {remaining_quarts} quarts")
    print("or")
    print(f"{total_ounces} ounces")

if __name__ == "__main__":
    main()