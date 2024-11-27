import random
import re
from typing import List, Tuple, Optional
import typer

app = typer.Typer()


class Die:
    def __init__(self, sides: int):
        self.sides = sides

    def roll(self) -> int:
        """Rolls the die and returns the result."""
        return random.randint(1, self.sides)


class DieCollection:
    def __init__(self):
        self.dice: List[Tuple[int, Die]] = []

    def add_dice(self, num_dice: int, sides: int):
        """Adds a number of dice with the specified sides to the collection."""
        die = Die(sides)
        self.dice.append((num_dice, die))

    def roll_all(self) -> List[int]:
        """Rolls all dice in the collection and returns the results."""
        rolls = []
        for num_dice, die in self.dice:
            rolls.extend(die.roll() for _ in range(num_dice))
        return rolls


def parse_dice_notation(dice: str) -> DieCollection:
    """
    Parses a dice notation string into a DieCollection representing
    the number of dice and the number of sides.

    Args:
        dice (str): The dice notation string (e.g., "2d6", "3d10+2").

    Returns:
        DieCollection: A DieCollection object containing the parsed dice.

    Raises:
        ValueError: If the dice notation is invalid.
    """
    # Regular expression to match dice notation
    dice_regex = r"(\d*)d(\d+)([+-]\d+)?"
    matches = re.findall(dice_regex, dice)

    if not matches:
        raise ValueError(f"Invalid dice notation: {dice}")

    die_collection = DieCollection()
    for match in matches:
        num_dice = int(match[0]) if match[0] else 1  # Default to 1 if not specified
        num_sides = int(match[1])
        die_collection.add_dice(num_dice, num_sides)

    return die_collection


def calculate_total(rolls: List[int], modifier: Optional[int] = 0) -> int:
    """
    Calculates the total of the dice rolls including a modifier.

    Args:
        rolls (List[int]): The list of dice rolls.
        modifier (Optional[int]): An optional modifier to add to the total.

    Returns:
        int: The total value of the rolls plus the modifier.
    """
    return sum(rolls) + (modifier if modifier else 0)


@app.command()
def roll(dice: str):
    """
    Rolls dice according to the provided notation and prints the results.

    Args:
        dice (str): The dice notation (e.g., "2d6+3").
    """
    try:
        # Parse the dice notation and get a DieCollection
        die_collection = parse_dice_notation(dice)

        # Roll all dice in the collection
        total_rolls = die_collection.roll_all()

        # Check for modifiers in the input
        modifier_match = re.search(r"([+-]\d+)$", dice)
        total_modifier = int(modifier_match.group(0)) if modifier_match else 0

        # Calculate total
        total = calculate_total(total_rolls, total_modifier)

        # Output results
        typer.echo(f"Rolls: {total_rolls}")
        typer.echo(f"Total: {total}")

    except ValueError as e:
        typer.echo(f"Error: {e}")


if __name__ == "__main__":
    app()
