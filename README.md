# Who Wants to Be a Millionaire — Simple Python Edition

A small console-based implementation of the classic quiz game "Who Wants to Be a Millionaire" written in Python. This project provides a minimal playable experience with lifelines and a short question set, intended for learning and extension.

## Features

- Console-based interactive gameplay
- Two lifelines: `50-50` and `audience`
- Simple question list defined in `main.py`

## Requirements

- Python 3.7 or newer

## Run

Open a terminal in the project folder and run:

```bash
python main.py
```

Use the following controls during the game:

- Answer: `A`, `B`, `C`, or `D`
- Lifelines menu: `L` (then type `50-50` or `audience`)
- Quit and take current money: `Q`

## Adding Questions

Questions are stored in the `QUESTIONS` list inside `main.py`. Each question entry is a dict with keys:

- `q` — question text
- `options` — list of four answer strings
- `answer` — index (0-based) of the correct option
- `money` — prize amount for that question

Example:

```python
{
    "q": "Sample question?",
    "options": ["Opt A", "Opt B", "Opt C", "Opt D"],
    "answer": 0,
    "money": 100,
}
```

## Extending the Game

Ideas to expand the project:

- Load questions from a JSON or CSV file
- Add more lifelines (phone-a-friend, switch the question)
- Persist high scores
- Add timed questions

## License

This project is provided as-is for learning purposes.
