# Python Syntax Scanner

A lightweight command-line tool that scans a Python project and detects **syntax errors** before any script is executed.

## 🚀 Features

- Recursively scans all `.py` files in a given directory.
- Detects and reports **syntax errors** using Python's built-in `ast` module.
- Displays results grouped by file and line number.
- Prints clean, colorless console output for easy redirection or CI integration.
- Uses only the Python standard library — no external dependencies.

## 🧠 Usage

Run the scanner from the command line and provide a directory path to analyze:

```bash
python scanner.py <project_root>
