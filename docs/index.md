# Turtle Tags: Code Your Initials in Python 🐢

**Session Title:** Turtle Tags: Code Your Initials in Python  
**Session Length:** ~18 minutes  
**Audience:** Middle & High School Students (no prior coding experience needed)

## Session Description

Ever wanted to sign your name with code? In this mini-session, students use Python’s
Turtle Graphics to bring their initials to life on the screen. They’ll learn how to make
a virtual turtle draw shapes, lines, and letters with simple commands. It’s quick, creative,
and they walk away with their own digital “signature” coded in Python.

## What Students Will Learn

- Basic Python commands for movement and drawing:
  - `forward()`, `left()`, `right()`
  - `penup()`, `pendown()`
  - `goto(x, y)`
- How to think in simple steps (algorithms) to draw letters.
- How small code changes affect what they see on the screen.

## Running the Activity

1. Open a terminal in the project folder.
2. Run:

   ```bash
   python activity/initials.py
   ```

3. A window will open showing the turtle drawing some sample initials and confetti.

Teachers can invite students to:
- Modify the starting positions of the letters.
- Change sizes, colors, and line thickness.
- Replace the sample initials with their own.

## Quick Turtle Command Cheat Sheet

```python
t.forward(100)    # move forward 100 pixels
t.right(90)       # turn right 90 degrees
t.left(90)        # turn left 90 degrees
t.penup()         # lift pen (no drawing)
t.pendown()       # place pen (draw again)
t.goto(0, 0)      # jump to position (0, 0)
t.color("blue")   # change pen color
t.pensize(6)      # change line thickness
```

## Resetting Between Sessions (Teachers)

To quickly reset the repository between student groups:

- **Windows:** double-click `scripts/reset.bat`
- **Mac/Linux:** run:

  ```bash
  ./scripts/reset.sh
  ```

This returns the files to their last committed state, removing any changes students made.

## Ideas for Extension

- Animate the initials with a small loop (wiggling or pulsing effect).
- Add a simple shape or logo next to the initials.
- Change the background color and confetti style.
