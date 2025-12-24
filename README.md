# Python Concepts Repository

A personal reference and playground for Python concepts I want to remember — from syntax basics to advanced patterns.

---

## 📁 Structure

| Folder           | Description                                            |
|------------------|--------------------------------------------------------|
| **basics/**      | Core language features: variables, loops, control flow |
| **cli/**         | Command line interface scripts                         |
| **collections/** | Lists, Dictionaries, Sets, and Tuples                  |
| **concurrency/** | Multithreading                                         |
| **functional/**  | Lambdas, functions, exceptions, kwargs                 |
| **io/**          | Input/output operations                                |
| **oop/**         | Object-oriented principles — classes, inheritance      |
| **snippets/**    | Miscellaneous utilities and small experiments          |
| **tests/**       | Unit testing                                           |

---

## 🧩 How to use
Each folder contains runnable examples and a `notes.md` file with short explanations, gotchas, and tips.

You can run examples using:
```bash
python3 module_name.py
```

---

## Create Python Virtual Environment
`python3 -m venv .venv`

- Activate python virtual environment:
  - `source .venv/bin/activate`

- Leave python virtual environment:
  - `deactivate`

---

## Create requirements.txt and Install
- `pip freeze > requirements.txt`
- `pip install -r requirements.txt`

## Modules
- A module is essentially a file in python
- A package is essentially a folder in python
- <i>A package is a collection of modules</i>