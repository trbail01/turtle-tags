# Turtle Tags: Code Your Initials in Python

**Length:** ~18 minutes · **Audience:** Middle & High School Beginners · **Tech:** Python 3 (standard library only)

This activity gives students a fast, visual introduction to Python using Turtle Graphics.
In one short session, they’ll write code to draw their initials on screen and add a fun “confetti” effect.

## Quick Start (Teacher)

1. Install Python 3 on each machine (if not already installed).
2. Clone or download this repository to each lab computer.
3. Open a terminal in the project folder and run:

```bash
python activity/initials.py
```

4. Between student groups, run the reset script:
   - **Windows:** double-click `scripts/reset.bat`
   - **Mac/Linux:** run `./scripts/reset.sh` from the project folder

## Flow for an 18-Minute Session

**0–3 minutes – Intro & Demo**

- Show the students the turtle window.
- Point out a few commands:
  ```python
  t.forward(100)
  t.right(90)
  t.left(90)
  t.penup()
  t.pendown()
  t.goto(0, 0)
  t.color("red")
  ```
- Briefly run the starter code to show how a letter can be drawn.

**3–10 minutes – Students Draw Their First Letter**

- Have students open `activity/initials.py` or a copy of it.
- Ask them to focus on just the *first* letter of their initials.
- Encourage rough block letters, not perfect handwriting.

**10–15 minutes – Add Style**

- Students add:
  - A second letter (or all initials).
  - Colors (`t.color("blue")`) and thicker lines (`t.pensize(8)`).
  - The confetti effect (already included at the bottom of `initials.py`).

**15–18 minutes – Show & Reset**

- Have a quick share-out: a few volunteers run their programs on the projector.
- Run the reset script before the next group.

## Files & Folders

- `activity/initials.py` – main starter activity file.
- `activity/letters.py` – optional helper functions for drawing letters.
- `activity/examples/` – space for pre-made examples (you can add more).
- `scripts/reset.bat` – reset changes on Windows using Git.
- `scripts/reset.sh` – reset changes on macOS/Linux using Git.
- `scripts/run.bat` – one-click launcher on Windows.
- `docs/index.md` – GitHub Pages site content.

## Stretch Ideas

- Make the initials animate slightly (small wiggles in a loop).
- Draw a box or underline around the initials.
- Change the background color or confetti colors.
- Have students add their favorite shape (star, heart, etc.) next to their initials.

## License

This project is released under the MIT License. Feel free to adapt it for your classes.
