import ast
import sys
import traceback

def fix_missing_colons(code_lines):
    keywords = ['if', 'elif', 'else', 'for', 'while', 'def', 'class', 'try', 'except', 'finally', 'with']
    fixed_lines = []
    for line in code_lines:
        stripped = line.strip()
        if any(stripped.startswith(k) for k in keywords):
            if not stripped.endswith(':'):
                line = line.rstrip() + ':'
        fixed_lines.append(line)
    return fixed_lines

def fix_unbalanced_parentheses(code):
    open_paren = code.count('(')
    close_paren = code.count(')')
    if open_paren > close_paren:
        code += ')' * (open_paren - close_paren)
    elif close_paren > open_paren:
        code = '(' * (close_paren - open_paren) + code
    return code

def try_parse(code):
    try:
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, e

def main():
    filename = input("Enter filename of Python code to fix and run: ")
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    code = ''.join(lines)
    valid, error = try_parse(code)
    if valid:
        print("Code parses fine, running it...")
        exec(code)
        return

    lines = fix_missing_colons(lines)
    code = ''.join(lines)
    valid, error = try_parse(code)
    if valid:
        print("Fixed missing colons. Running fixed code...")
        exec(code)
        return

    code = fix_unbalanced_parentheses(code)
    valid, error = try_parse(code)
    if valid:
        print("Fixed unbalanced parentheses. Running fixed code...")
        exec(code)
        return

    print("Could not automatically fix syntax errors.")
    print("Error details:")
    traceback.print_exception(type(error), error, error.__traceback__)

if __name__ == "__main__":
    main()
