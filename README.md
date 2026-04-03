# GUI Distance Unit Converter

A tkinter-based desktop GUI application that converts distances between kilometers and miles.

---

## Features

- Convert **kilometers to miles** or **miles to kilometers** via radio button selection
- Results displayed inline with 2 decimal places of precision
- Input validation with a user-friendly error message for non-numeric input
- **Clear/Refresh** button to reset the input field and result label
- **Quit** button to close the application

## Requirements

- Python 3.x
- `tkinter` (included with standard Python installations)

## Usage

1. Enter a numeric distance value in the input field.
2. Select a conversion direction using the radio buttons:
   - **Kilometers to Miles** — divides by `1.60934`
   - **Miles to Kilometers** — multiplies by `0.62139`
3. The result appears immediately in the result label.
4. Use **Clear/Refresh** to reset, or **Quit** to exit.

## Conversion Formulas

| Conversion | Formula |
|---|---|
| Kilometers → Miles | `miles = km / 1.60934` |
| Miles → Kilometers | `km = miles * 0.62139` |

## GUI Layout

| Element | Description |
|---|---|
| Entry field | Accepts the numeric distance input |
| Radio buttons | Selects conversion direction (triggers calculation on click) |
| Result label | Displays the converted value or an error message |
| Clear/Refresh | Clears the entry field and resets the result label |
| Quit | Closes the application window |
