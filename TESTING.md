# Testing Strategy (Quick-Calc)

## Overview
This project uses two layers of tests:
- **Unit tests** validate each calculator operation in isolation (add, subtract, multiply, divide, clear).
- **Integration tests** validate higher-level usage scenarios using the calculator component.

## Concepts (Lecture Alignment)

### Testing Pyramid
Most tests are unit tests because they are fast and cover core logic. A smaller set of integration tests validates key flows.

### Black-box vs White-box
Unit tests are closer to white-box testing (direct method calls). Integration tests are closer to black-box testing (scenario-based behavior).

### Functional Testing
The suite focuses on functional correctness: expected outputs and safe handling of division by zero.

### Regression Testing
Running `pytest` after changes helps detect if new edits break existing functionality.
