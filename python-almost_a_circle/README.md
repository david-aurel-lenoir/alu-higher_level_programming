# Python - Almost a circle

This project is part of the Higher Level Programming curriculum (ALU).
It implements a `Base` class along with `Rectangle` and `Square` classes
that inherit from it, following an object-oriented approach in Python 3.

## Description

- `Base`: manages the `id` attribute for every future class, and provides
  serialization helpers (JSON, CSV).
- `Rectangle`: represents a rectangle with `width`, `height`, `x`, `y`.
- `Square`: represents a square, inheriting from `Rectangle`.

## Requirements

- Python 3.8+
- PEP 8 style (pycodestyle)
- All classes, methods, and functions must be documented and unit tested.

## Usage

```bash
python3 -m unittest discover tests
pycodestyle models/ tests/
```

## Author

Guillaume
