"""A simple command-line tool for rolling dice using dice notation."""

import random
import re
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as get_version
from typing import List, Optional, Tuple

import typer

app = typer.Typer(rich_markup_mode="markdown")


class Die:
    """A class representing a die with a number of sides."""

    def __init__(self, sides: int):
        """Initialize the die with the number of sides."""
        self.sides = sides

    def roll(self) -> int:
        """Roll the die and returns the result."""
        return random.randint(1, self.sides)


class DieCollection:
    """A class representing a collection of dice with different numbers of sides."""

    def __init__(self):
        """Initialize the collection of dice."""
        self.dice: List[Tuple[int, Die]] = []

    def add_dice(self, num_dice: int, sides: int):
        """Add a number of dice with the specified sides to the collection."""
        die = Die(sides)
        self.dice.append((num_dice, die))

    def roll_all(self) -> List[int]:
        """Roll all dice in the collection and returns the results."""
        rolls = []
        for num_dice, die in self.dice:
            rolls.extend(die.roll() for _ in range(num_dice))
        return rolls


def parse_dice_notation(dice: str) -> DieCollection:
    """Parse a die notation string into a DieCollection representing the number of dice and the number of sides.

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
    """Calculate the total of the dice rolls including a modifier.

    Args:
        rolls (List[int]): The list of dice rolls.
        modifier (Optional[int]): An optional modifier to add to the total.

    Returns:
        int: The total value of the rolls plus the modifier.

    """
    return sum(rolls) + (modifier or 0)


def version_callback(value: bool):
    if value:
        try:
            version = get_version("roll")
            typer.echo(f"Version: {version}")
        except PackageNotFoundError:
            typer.echo("Version information not available.")
        raise typer.Exit()


die_roll_help = """
given in the form AdX. A and X are variables, separated by the letter d, which stands for die or dice.  
- A is the number of dice to be rolled (omitted if 1).
- X is the number of faces of each die. The faces are numbered from 1 to X, with the assumption that the die generates a random integer in that range, with uniform probability.
"""


@app.command()
def roll(
    dice: str = typer.Argument(None, help=die_roll_help),
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        help="Display the version of the tool.",
    ),
):
    """Roll dice according to the provided notation and prints the results.

    Args:
        dice (str): The dice notation (e.g., "2d6+3").
        version (bool): Flag to display the version of the tool.

    """
    try:
        # Parse the dice notation and get a DieCollection
        die_collection = parse_dice_notation(dice)

        # Roll all dice in the collection
        total_rolls = die_collection.roll_all()

        # Check for modifiers in the input
        modifier_match = re.search(r"([+-]\d+)$", dice)
        total_modifier = int(modifier_match[0]) if modifier_match else 0

        # Calculate total
        total = calculate_total(total_rolls, total_modifier)

        # Output results
        typer.echo(f"Rolls: {total_rolls}")
        typer.echo(f"Total: {total}")

    except ValueError as e:
        typer.echo(f"Error: {e}")


if __name__ == "__main__":
    app()
