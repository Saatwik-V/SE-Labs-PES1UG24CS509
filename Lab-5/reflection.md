# Lab 5: Static Code Analysis - Reflection

### 1. What is static code analysis and how does it help?
Static code analysis involves examining source code without executing the program. It helps find bugs, logical errors, security vulnerabilities, and formatting issues early in development, before code reaches testing or production.

### 2. How do Pylint, Bandit, and Flake8 complement each other?
- **Bandit** acts as a security scanner, checking for dangerous functions, SQL injections, and weak cryptographic practices.
- **Pylint** analyzes code quality, programming logic, naming conventions, and structural design (like mutable default arguments).
- **Flake8** ensures code conforms to standard PEP 8 formatting rules, such as line length, whitespace, and variable naming clarity.

Using all three provides full coverage across security, logic, and readability.

### 3. Why were certain issues prioritized over others?
High and medium severity issues were prioritized first:
1. The **SQL Injection** risk in the `INSERT` query and the **MD5 hash** warning from Bandit were fixed first because security vulnerabilities can directly compromise data safety.
2. The **mutable default argument (`extras={}`)** flagged by Pylint was fixed next because sharing a mutable object across function calls causes real runtime logic bugs.
3. Style issues like line length and whitespace from Flake8 were addressed last because they affect code readability rather than security or correctness.

### 4. What was the impact of the fixes?
- Pylint score improved from **3.46/10** to a perfect **10.00/10**.
- Bandit security issues dropped from **3** to **0**.
- Flake8 style violations dropped from **6** to **0**.
- The program continues to execute properly with identical output (`5455c3 25 Leopard`), but is now secure, PEP 8 compliant, and maintainable.
