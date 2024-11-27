# Dice Rolling Application

This is a simple command-line application for rolling dice based on user-defined notation. The application allows users to specify how many dice to roll and the number of sides on each die, as well as any modifiers to the total roll.

## Features

-    Parse dice notation such as `2d6`, `3d10+2`, and `1d20-1`.
-    Roll multiple dice at once.
-    Calculate the total of the rolls including any modifiers.
-    Display the results in a user-friendly format.

## Requirements

-    Python 3.7 or higher
-    Typer library for command-line interface

You can install Typer using pip:

```bash
pip install typer
```

## Installation

1. Clone the repository:

  ```bash
   git clone https://github.com/yourusername/dice-roller.git
   cd dice-roller
   ```

2. Install the required dependencies:

  ```bash
   pip install -r requirements.txt
   ```

## Usage

To roll dice, run the application with the desired dice notation. For example:

```bash
python dice_roller.py roll "2d6+3"
```

### Dice Notation

The dice notation follows the format:

```XdY[+/-Z]```

Where:
-    `X` is the number of dice to roll (default is 1 if omitted).
-    `Y` is the number of sides on each die.
-    `Z` is an optional modifier to add or subtract from the total roll.

### Examples

-    Roll two six-sided dice and add 3 to the total:

  ```bash
   python dice_roller.py roll "2d6+3"
   ```

-    Roll three ten-sided dice:

  ```bash
   python dice_roller.py roll "3d10"
   ```

-    Roll one twenty-sided die and subtract 1 from the total:

  ```bash
   python dice_roller.py roll "1d20-1"
   ```

## Code Overview

The main components of the application include:

1. **Die Class**: Represents a single die and provides functionality to roll it.

   ```python
   class Die:
       def __init__(self, sides: int):
           self.sides = sides

       def roll(self) -> int:
           """Rolls the die and returns the result."""
           return random.randint(1, self.sides)
   ``` 

2. **DieCollection Class**: Represents a collection of dice, allowing for multiple dice to be rolled together.

   ```python
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
   ``` 

3. **parse_dice_notation Function**: Parses the user input and returns a `DieCollection` representing the dice to be rolled.

   ```python
   def parse_dice_notation(dice: str) -> DieCollection:
       # Implementation...
   ``` 

4. **Roll Command**: The command-line interface that handles user input and displays the results.

   ```python
   @app.command()
   def roll(dice: str):
       # Implementation...
   ``` 

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
