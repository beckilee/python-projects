# Tic-Tac-Toe

This is a game for two players who take turns entering an X or an O on a 9-square grid. When someone gets three symbols in a row, in a column, or diagonally, they win!

The script keeps score of how many games each player has won during the session, and the score is reset when the script exits.

## Setup

1. Clone this repo:

	```
	git clone https://github.com/beckilee/python-projects.git
	```

2. Move into the `python-projects/tic-tac-toe` directory:

	```
	cd python-projects/tic-tac-toe
	```

## How to play

To play the game, enter the following command:

```
python tic-tac-toe.py
```

The first player is **X** and the second player is **O**.

When it's your turn, enter a number corresponding to a square:

```
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

The game draws your symbol in the square you select. For example, if player **X** enters the number `1`, the board looks like this:

```
 X |   |
-----------
   |   |
-----------
   |   |
```

Player **O** then takes their turn.

The game continues until someone wins by getting three symbols in a row, in a column, or diagonally.

After the game ends, enter `Y` to play again. To exit the script, enter anything else.

## Contact me!

If you liked this game, or if you have suggestions for improvements, drop me a line at becki.lee@gmail.com.