# Python Fundamentals

A curated collection of Python fundamentals implemented as small, focused scripts—designed for quick lookup, practice, and clean progression.

This repository is built while learning from the Platzi course:
https://platzi.com/cursos/fundamentos-python/

---

## What you’ll find

- Short scripts focused on one concept at a time
- Examples you can run locally (no heavy dependencies)
- A course-aligned roadmap (lesson by lesson)
- A learning repository with a “portfolio-ready” structure

---

## Repository structure

Most scripts live in the repository root and can be executed directly:

```bash
python3 python_data_types.py
```

Recommended (optional) virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

> Tip: If you are on Windows, use `py` instead of `python3` in some setups:
> `py python_data_types.py`

---

## Topics covered (current)

- Syntax, comments, variables
- Data types and casting (`bool`, numeric conversion, `None`)
- Operators (arithmetic, logical, assignment, walrus)
- Control flow (`if/else`, `match`)
- Loops (`while`)
- Strings (handling, search, slicing, replace, split)

---

## Roadmap (mapped to Platzi: Python Fundamentals)

This repository follows the course learning path:
https://platzi.com/cursos/fundamentos-python/

> ✅ = already covered in this repo  
> ⏳ = planned next

### Getting started with Python
- ✅ Why Instagram and NASA chose Python (notes)
- ✅ Install Python, VS Code and Git on Windows (notes)
- ✅ Configure environment variables for Python on Windows (notes)
- ✅ Basic Python commands in the Windows terminal (notes)
- ✅ Basic syntax and indentation in Python (VS Code)  
  Covered by: `syntax.py`
- ✅ Comments in Python (single-line and multi-line)  
  Covered by: `comments.py`
- ✅ Variables: assignment, naming and conventions  
  Covered by: `variables.py`
- ✅ Multiple variable assignment  
  Covered by: `python_multiple_variable_assignment.py`
- ✅ Data types: strings, numbers and collections  
  Covered by: `python_data_types.py`
- ✅ Numeric type conversion and manipulation  
  Covered by: `python_numeric_type_conversion.py`
- ✅ Quotes, multi-line strings and searching inside strings  
  Covered by: `python_string_handling.py`
- ✅ Slicing, replace and split for string manipulation  
  Covered by: `python_string_manipulation.py`
- ✅ Booleans: True/False and casting to bool  
  Covered by: `python_booleans_and_casting.py`
- ✅ None type  
  Covered by: `python_none_type.py`

### Programming logic & control flow
- ✅ Arithmetic operators: +, -, %, precedence  
  Covered by: `python_arithmetic_operators.py`
- ✅ Assignment operators and walrus operator  
  Covered by: `python_assignment_and_walrus_operator.py`
- ✅ Logical operators OR and NOT  
  Covered by: `python_logical_operators_or_not.py`
- ✅ Conditionals: if, else, and, or, pass  
  Covered by: `python_conditionals_if_else.py`
- ✅ match statement (Python 3.10+)  
  Covered by: `python_match_statement.py`
- ✅ while loops: conditions, break and continue  
  Covered by: `python_while_loops.py`
- ✅ for loops: iterating sequences and lists
  Covered by: `python_for_loops.py`

### Fundamental data structures
- ✅ Lists: creation, mutation and essential methods
  Covered by: `python_lists.py`
- ⏳ Tuples: ordered, immutable and duplicates  
  Planned: `python_tuples.py`
- ⏳ Sets: creation, methods and basic operations  
  Planned: `python_sets.py`
- ⏳ Dictionaries: ordered key-value pairs and nested dicts  
  Planned: `python_dicts.py`

### Code modularization
- ⏳ Functions: arguments and return  
  Planned: `python_functions_basics.py`
- ⏳ Lambda functions and function factory  
  Planned: `python_lambda_and_factory.py`
- ⏳ Modules: organizing code into multiple files  
  Planned: `python_modules_imports.py`

### Errors & files
- ⏳ Error handling: try, except, finally  
  Planned: `python_try_except_finally.py`
- ⏳ Read/write text files  
  Planned: `python_file_io_text.py`

### Final project
- ⏳ Coffee machine (interactive terminal menu)  
  Planned: `projects/coffee-machine/main.py`
- ⏳ Coffee project: read/write files (persistence)  
  Planned: `projects/coffee-machine/` + data file storage

---

## Contributing

This is a personal learning repository, but suggestions are welcome.

If you want to propose improvements:
1. Open an issue describing the change
2. Create a PR with small, focused edits (one topic per PR)

---

## License

MIT License (recommended for educational examples). See `LICENSE`.

---

## Credits

- Platzi course: https://platzi.com/cursos/fundamentos-python/
