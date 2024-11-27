# Roll Utility

The `roll` utility is a command-line tool for rolling dice using standard dice notation. It allows users to specify the number of dice, the number of sides on each die, and any modifiers to the total roll.

## Usage

You can run the utility from the command line as follows:

```
python roll.py "<dice-notation>"
```

### Dice Notation

Dice notation is a way to specify how many dice to roll and what type of dice to use. The general format is:

```
XdY[+/-Z]
```

Where:
-   **X**: The number of dice to roll (optional, defaults to 1 if omitted).
-   **Y**: The number of sides on each die (required).
-   **Z**: An optional modifier that can be added or subtracted from the total.

### Examples

1. **Single Die Roll**:
   - Notation: `d6`
   - Description: Rolls one six-sided die.
   - Output: `Rolls: [4]`, `Total: 4`

2. **Multiple Dice Roll**:
   - Notation: `3d8`
   - Description: Rolls three eight-sided dice.
   - Output: `Rolls: [5, 3, 7]`, `Total: 15`

3. **Dice Roll with Modifier**:
   - Notation: `2d10+5`
   - Description: Rolls two ten-sided dice and adds 5 to the total.
   - Output: `Rolls: [9, 6]`, `Total: 20`

4. **Dice Roll with Negative Modifier**:
   - Notation: `4d6-2`
   - Description: Rolls four six-sided dice and subtracts 2 from the total.
   - Output: `Rolls: [3, 5, 2, 4]`, `Total: 12`

5. **Complex Notation**:
   - Notation: `2d6+3d4-1`
   - Description: Rolls two six-sided dice and three four-sided dice, then subtracts 1 from the total.
   - Output: `Rolls: [4, 2, 1, 3, 4]`, `Total: 13`

## Error Handling

If the input dice notation is invalid, the utility will return an error message. For example, using an incorrect format like `2d+3` will result in:

```
Error: Invalid dice notation: 2d+3
```

## Conclusion

The `roll` utility is a simple and effective tool for rolling dice with various configurations. Whether you're a tabletop gamer or just need some random numbers, this utility can help you quickly generate the results you need.

Feel free to customize and expand this utility to fit your specific needs!
