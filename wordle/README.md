# Becki's Wordle Clone

This Python script is inspired by the popular word game [Wordle](https://www.nytimes.com/games/wordle/index.html). It was written with Python 3.9.7.

## Setup

1. Clone this repo:

	```
	git clone https://github.com/beckilee/python-projects.git
	```

2. Move into the `python-projects/wordle` directory:

	```
	cd python-projects/wordle
	```

## How to play

**IMPORTANT:** Becki's Wordle Clone needs to access the file [words.txt](./words.txt). Make sure you're in the `wordle` directory before you run the script:

```
python wordle.py
```

Try to guess the randomly selected 5-letter word. After you enter your guess, it is color-coded as follows:

- **Green:** Letter is in the correct place
- **Yellow:** Letter is in the wrong place
- **No color:** Letter is not in the word

Unlike the real Wordle, Becki's Wordle Clone gives you as many guesses as you need! So, if you don't get the answer right away, keep guessing.

When you get the answer, the game congratulates you and exits.

If you give up, simply enter:

```
I GIVE UP
```

The game prints the answer and exits.

## Future enhancements

- Use the Wordnik API to request a random 5-letter word instead of pulling from `words.txt`

## Contact me!

If you liked this game, or if you have suggestions for improvements, drop me a line at becki.lee@gmail.com.