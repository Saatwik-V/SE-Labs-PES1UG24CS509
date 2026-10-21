# Lab 5: Static Code Analysis & Security Linting

## Environment Setup

The Python virtual environment has already been created and the required tools are installed:
- **Pylint** (Static code analyzer)
- **Bandit** (Security vulnerability linter)
- **Flake8** (Style & PEP 8 guide enforcer)

---

## How to Activate the Virtual Environment

### If working inside the `Lab-5` directory:
```bash
cd Lab-5
source venv/bin/activate
```

### If working from the repository root:
```bash
source venv/bin/activate
```

*(To exit the environment when finished, simply run `deactivate`)*

---

## Tool Usage Quick Reference

### 1. Pylint
Analyzes code quality, conventions, and potential bugs:
```bash
pylint <filename.py>
```

### 2. Bandit
Scans code for common security issues and vulnerabilities:
```bash
bandit -r .                 # Recursive scan of the directory
bandit <filename.py>        # Scan a single file
```

### 3. Flake8
Checks adherence to PEP 8 style guidelines and syntax errors:
```bash
flake8 <filename.py>
flake8 .                    # Check all files in current directory
```
