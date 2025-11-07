import os
import ast
import sys

def scan_python_files(root_dir):
    issues = []
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(subdir, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        source = f.read()
                    ast.parse(source, filename=path)
                except SyntaxError as e:
                    issues.append((path, e.lineno, e.msg))
    return issues


def main():
    if len(sys.argv) < 2:
        print("Usage: python scanner.py <project_root>")
        sys.exit(1)

    root = sys.argv[1]
    issues = scan_python_files(root)

    if not issues:
        print("No syntax errors found.")
    else:
        print("Syntax errors detected:\n")
        for path, line, msg in issues:
            print(f"{path}:{line} — {msg}")


if __name__ == "__main__":
    main()
