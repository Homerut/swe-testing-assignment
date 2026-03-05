# Quick-Calc

Quick-Calc is a basic calculator application created for the Advanced Software Engineering practical assignment.
It supports:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/) with graceful division-by-zero handling
- Clear (C)

The focus of the project is clean, testable code and a multi-layered testing strategy (unit + integration tests) managed with Git/GitHub.

## Setup Instructions

This project requires Python 3.

(Optional but recommended) create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m quick_calc.cli
> 5 + 3
Result: 8.0
> 8 / 0
Error: Cannot divide by zero
> C
Result: 0
> exit
pytest
