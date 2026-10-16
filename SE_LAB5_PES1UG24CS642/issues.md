# Lab 5: Static Code Analysis — Online Examination System

## 1. Objective

The objective of this lab was to analyze the original Python program using
Pylint, Bandit, and Flake8, identify code quality, security, and style issues,
and improve the code while preserving its functionality.

## 2. Issues Identified and Fixed

| No. | Issue Found in Original Code | Tool | Severity | Before (Original Code) | After (Fixed Code) | Fix Explanation |
|---|---|---|---|---|---|---|
| 1 | Inappropriate random generator | Bandit (B311) | Low | `random.choice(QUESTIONS)` | `secrets.choice(QUESTIONS)` | Replaced the standard random generator with the secrets module to use a security-appropriate random selection method. |
| 2 | Mutable default argument | Pylint (W0102) | Code quality | `def grade_student(student_name, responses, penalties={}):` | `def grade_student(student_name, responses, penalties=None):` | Avoided sharing a mutable dictionary between function calls by using None as the default and initializing the dictionary inside the function. |
| 3 | Non-standard function and parameter names | Pylint (C0103) | Code style | `def hashAnswer(text):` | `def hash_answer(text):` | Changed function and parameter names to follow Python's snake_case naming convention. |
| 4 | Missing function docstrings | Pylint (C0116) | Code quality | `def get_grade(score):` | `def get_grade(score):` followed by a descriptive docstring | Added docstrings to explain the purpose of functions. |
| 5 | Inefficient loop style | Pylint (C0200) | Code quality | `for i in range(len(QUESTIONS)):` | `for i, question in enumerate(QUESTIONS):` | Used enumerate to iterate through the questions and obtain their indices. |
| 6 | Unnecessary elif after return | Pylint (R1705) | Code quality | `elif percent >= 60:` | `if percent >= 60:` | Removed the unnecessary elif because the preceding condition already returns when satisfied. |
| 7 | Unsafe shell command construction | Security review | Potential security risk | `os.system("ssh " + lab_pc + " lock-screen")` | Removed the unused function and its associated import, if applicable. | Avoided constructing a shell command using a variable, which could introduce command-injection risk. |

## 3. Original Analysis Results

- Pylint score before improvements: 5.65/10
- Bandit identified one low-severity issue (B311).
- Flake8 identified a spacing violation (E271).

## 4. Final Analysis Results

- Pylint score after improvements: 10.00/10
- Bandit: No issues identified.
- Flake8: No style violations reported.

## 5. Conclusion

Static analysis helped identify security, code quality, and style issues
in the original online examination program. The code was improved by
addressing the identified issues, and the final version was checked using
Pylint, Bandit, and Flake8. The program was also tested to verify that
its expected grading functionality remained intact.