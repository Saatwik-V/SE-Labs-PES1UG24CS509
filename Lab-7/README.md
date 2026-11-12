# L6_L7_21_gym_membership — Gym Membership

Lab 7: Fuzzing for Input Validation Bugs

## Summary

Used property-based fuzz testing with **Hypothesis** to uncover input validation crashes and edge-case bugs in `gym_membership.py`, then hardened all three functions (`parse_plan`, `calculate_bmi`, and `average_workout`) against invalid, malformed, and boundary inputs (`None`, missing/extra delimiters, empty inputs, `ZeroDivisionError`, `OverflowError`, `nan`/`inf`, and negative values).

## Files

| File | Description |
|------|-------------|
| `gym_membership.py` | Hardened gym membership utility script with input validation |
| `test_gym_membership.py` | Hypothesis fuzz tests covering all three functions (6/6 passing) |
| `Lab_7_FuzzTesting_PES1UG24CS509.pdf` | Lab 7 report containing terminal screenshots (Steps 2, 4, 5, and 6) |

## Running

```bash
python gym_membership.py
pytest test_gym_membership.py
```
