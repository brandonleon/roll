import random
import re
from typing import List, Tuple, Optional
import typer

app = typer.Typer()


def parse_dice_notation(dice: str) -> List[Tuple[int, int]]:
    """
    Parses a dice notation string into a list of tuples representing
    the number of dice and the number of sides.

    Args:
        dice (str): The dice notation string (e.g., "2d6", "3d10+2").

    Returns:
        List[Tuple[int, int]]: A list of tuples where each tuple contains
        two integers: (number of dice, number of sides).

    Raises:
        ValueError: If the dice notation is invalid.
    """
    # Regular expression to match dice notation
    dice_regex = r"(\d*)d(\d+)([+-]\d+)?"
    matches = re.findall(dice_regex, dice)

    if not matches:
        raise ValueError(f"Invalid dice notation: {dice}")

    parsed_dice = []
    for match in matches:
        num_dice = int(match[0]) if match[0] else 1  # Default to 1 if not specified
        num_sides = int(match[1])
        parsed_dice.append((num_dice, num_sides))

    return parsed_dice


def roll_dice(num_dice: int, num_sides: int) -> List[int]:
    """
    Rolls a specified number of dice with a given number of sides.

    Args:
        num_dice (int): The number of dice to roll.
        num_sides (int): The number of sides on each die.

    Returns:
        List[int]: A list of integers representing the results of each die roll.
    """
    return [random.randint(1, num_sides) for _ in range(num_dice)]


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
        # Parse the dice notation
        parsed_dice = parse_dice_notation(dice)

        total_rolls = []
        total_modifier = 0

        # Roll each set of dice
        for num_dice, num_sides in parsed_dice:
            rolls = roll_dice(num_dice, num_sides)
            total_rolls.extend(rolls)

        # Check for modifiers in the input
        modifier_match = re.search(r"([+-]\d+)$", dice)
        if modifier_match:
            total_modifier = int(modifier_match.group(0))

        # Calculate total
        total = calculate_total(total_rolls, total_modifier)

        # Output results
        typer.echo(f"Rolls: {total_rolls}")
        typer.echo(f"Total: {total}")

    except ValueError as e:
        typer.echo(f"Error: {e}")


if __name__ == "__main__":
    app()
