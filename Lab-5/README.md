# Lab 5: Static Code Analysis

## Overview
In this lab, we performed static code analysis on the assigned Python script (`wildlife_sightings.py`) using three industry-standard tools: **Bandit**, **Pylint**, and **Flake8**. We identified security vulnerabilities, logic and quality issues, and PEP 8 style violations, documented them, and fixed them in three targeted commits.

---

## Summary of Work Done

### 1. Bandit (Security Analysis)
- **SQL Injection (`B608`)**: Replaced string interpolation (`.format()`) with parameterized queries (`?` placeholders) in the SQL `INSERT` statement.
- **Weak MD5 Hash (`B324`)**: Added `usedforsecurity=False` in `hashlib.md5()` to clarify that the hash is purely for short observer display IDs.
- **Assert Statement (`B101`)**: Replaced `assert` with a standard `if` condition and exception.
- **Result**: Security issues reduced from **3** to **0**.

### 2. Pylint (Code Quality & Logic)
- **Mutable Default Argument (`W0102`)**: Changed `extras={}` to `extras=None` and initialized `extras = {}` inside `log_sighting` to prevent state retention across function calls.
- **Variable Shadowing (`W0621`)**: Moved database setup to an `init_db()` function and renamed parameters to `connection` to avoid shadowing outer scope variables.
- **Naming Conventions (`C0103`)**: Converted function names to standard snake_case (`log_sighting`, `observer_id`, `zone_summary`).
- **Docstrings & Clean Code (`C0114`, `C0116`, `R1705`)**: Added module and function docstrings, and removed redundant `else` after return.
- **Result**: Pylint score improved from **3.46 / 10** to **10.00 / 10**.

### 3. Flake8 (PEP 8 Style & Formatting)
- **Line Length (`E501`)**: Wrapped lines so all statements remain strictly within the standard 79-character limit.
- **Ambiguous Variable Name (`E741`)**: Renamed single-letter variable `l` to `rarest_species`.
- **Operator Spacing (`E225`)**: Added standard whitespace around operators.
- **Result**: Style violations reduced from **6** to **0**.

---

## Deliverables in this Folder

- `wildlife_sightings.py`: Cleaned, secure, and fully working Python script.
- `issues.md`: Detailed table documenting the identified issues, line numbers, and fixes.
- `reflection.md`: Answers to the reflection questions based on the lab outcomes.
- `pylint_report_before.txt` & `pylint_report_after.txt`
- `bandit_report_before.txt` & `bandit_report_after.txt`
- `flake8_report_before.txt` & `flake8_report_after.txt`
- `requirements.txt`: Python dependencies for the lab.

---

## How to Run

1. Activate virtual environment:
   ```bash
   cd Lab-5
   source venv/bin/activate
   ```

2. Run the script:
   ```bash
   python wildlife_sightings.py
   # Expected Output: 5455c3 25 Leopard
   ```

3. Run the tools:
   ```bash
   pylint wildlife_sightings.py
   bandit -r wildlife_sightings.py
   flake8 wildlife_sightings.py
   ```
