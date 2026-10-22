# Static Code Analysis - Issues Table

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| SQL Injection Risk | Security (Bandit B608) | 9 | Used string .format() to build SQL query, which can allow SQL injection. | Use parameterized queries with ? placeholders. |
| Insecure MD5 Hash | Security (Bandit B324) | 15 | hashlib.md5() is flagged as a weak hash function. | Add usedforsecurity=False since this is only a short observer ID. |
| Use of Assert | Security (Bandit B101) | 36 | assert is removed if Python runs in optimized mode (-O). | Replace assert with standard if condition and exception. |
| Mutable Default Argument | Bug (Pylint W0102) | 8 | extras={} is shared across all function calls, retaining old values. | Set default to None and initialize extras = {} inside function. |
| Variable Name Shadowing | Code Quality (Pylint W0621) | 8, 18, 26 | Parameter conn redefines the global conn variable from line 4. | Rename parameter to connection. |
| Unnecessary Else Block | Code Quality (Pylint R1705) | 20 | else block after return is redundant. | Remove else and return directly. |
| Ambiguous Variable Name | Style (Flake8 E741) | 28 | Single letter 'l' is ambiguous and hard to read. | Rename variable to rarest_species. |
| Missing Whitespace | Style (Flake8 E225) | 28 | l=min missing spaces around operator. | Add spaces around '='. |
| Line Too Long | Style (Flake8 E501) | 5, 9, 19, 27 | Lines exceed 79 characters. | Break long lines across multiple lines. |
