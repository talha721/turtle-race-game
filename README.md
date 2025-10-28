# Turtle Race Game

A small, beginner-friendly graphical game built with Python's standard `turtle` module.

This repository contains a simple turtle race implementation (`main.py`) where multiple turtles race across the screen and the user can bet on which color will win.

---

## Quick overview

- Language: Python (standard library only)
- UI: Python `turtle` graphics (requires a desktop GUI environment)
- Purpose: Learning exercise for working with graphics, simple game loops, and user input

---

## Features (current)

- Six turtles (colors: red, orange, yellow, green, blue, purple) start at the left and race to the right.
- A text input box asks the user to enter the color they want to bet on before the race starts.
- The turtles move forward by random increments until one crosses the finish line.
- The game prints to the console whether the user won or lost.

---

## Requirements

- Python 3.7 or newer
- No external packages required (uses the standard library)
- A graphical desktop environment (Windows, macOS, or Linux with an X server)

Note: `turtle` will not open a window on headless environments (for example, WSL without an X server or a remote CI runner without a display).

---

## How to run (Windows example)

1. Open a Command Prompt in the project directory (the directory that contains `main.py`).

2. Run:

   ```cmd
   python main.py
   ```

3. A window will open and a text input dialog will ask: "Which turtle will win the race? Enter the color:". Type one of the following color names exactly: `red`, `orange`, `yellow`, `green`, `blue`, or `purple` and press OK.

4. The race will start (if you entered a bet). When a turtle crosses the right edge the result will be printed to the console.

---

## Current behavior notes (about `main.py`)

- The code creates 6 turtles and places them at fixed vertical positions.
- All turtles start near the left edge (x = -370) and race toward the right edge (finish line around x = 380).
- Movement is randomized using `random.randint(0, 10)` each loop iteration.
- The script currently prints the result (win/lose) to the console; it does not show an on-screen message.

If you'd like, I can update `main.py` to:

- Show a pop-up or on-screen text announcing the winner,
- Add a restart button or keyboard controls,
- Add command-line options to run automated races for testing,
- Or add unit-testable movement logic (seeded randomness) so results can be deterministic in tests.

---

## Customization ideas

- Add a visible finish line and a scoreboard.
- Allow keyboard input to start/stop or choose a turtle.
- Add obstacles or power-ups that change a turtle's speed.
- Save high scores to a JSON file.

---

## Troubleshooting

- No window appears: confirm you're running on a machine with a GUI. On Linux, run with an X server available.
- The input box doesn't show: some platforms may block or change how `turtle` dialogs appear — try running in a regular system Python interpreter (not a headless or embedded environment).
- You entered a color that isn't accepted: type one of the exact color names listed above.

---

## Development

- Code entry point: `main.py`.
- I recommend running `main.py` locally and experimenting with the values in the `colors`, `x_positions`, and `y_positions` lists to change the race layout.

If you want, I can also:

- Improve `main.py` to include in-window messages and a restart flow.
- Add a small test harness and a `requirements.txt` if external packages are later introduced.

---

## License

This project is provided under the MIT License. Use and modify freely.

---

If you want any of the following, tell me which and I'll implement it next:

- Improve `main.py` UI (on-screen winner announcement + restart button)
- Add screenshots / GIFs to the README
- Add deterministic test harness for race logic
