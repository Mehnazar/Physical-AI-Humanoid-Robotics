#!/usr/bin/env python3
"""
Validate code examples for Physical AI & Humanoid Robotics Book

This script validates all Python code examples in the code-examples/ directory:
- Checks for required docstring header
- Verifies prerequisites section exists
- Verifies expected output section exists
- Verifies last validated date is recent (<30 days)
- Runs Python syntax check (ast.parse)
- Reports validation status per example

Reference: specs/001-physical-ai-book/plan.md:173, tasks.md:T072
"""

import ast
import os
import sys
from pathlib import Path
from datetime import datetime, timedelta
import re

def validate_example(file_path):
    """Validate a single code example file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []

    # Check for docstring header
    if not content.startswith('"""') and not content.startswith("'''"):
        errors.append("Missing docstring header")

    # Check for Prerequisites section
    if 'Prerequisites:' not in content and 'prerequisites:' not in content:
        errors.append("Missing Prerequisites section")

    # Check for Expected Output section
    if 'Expected Output:' not in content and 'expected output:' not in content:
        errors.append("Missing Expected Output section")

    # Check for Last Validated date
    validated_match = re.search(r'Last Validated:\s*(\d{4}-\d{2}-\d{2})', content, re.IGNORECASE)
    if not validated_match:
        errors.append("Missing Last Validated date")
    else:
        validated_date = datetime.strptime(validated_match.group(1), '%Y-%m-%d')
        if datetime.now() - validated_date > timedelta(days=30):
            errors.append(f"Last validated date is old: {validated_match.group(1)}")

    # Check Python syntax
    try:
        ast.parse(content)
    except SyntaxError as e:
        errors.append(f"Syntax error: {e}")

    return errors

def main():
    """Main validation function"""
    code_examples_dir = Path('code-examples')

    if not code_examples_dir.exists():
        print("Error: code-examples/ directory not found")
        return 1

    python_files = list(code_examples_dir.rglob('*.py'))

    if not python_files:
        print("No Python files found in code-examples/")
        return 0

    print(f"Validating {len(python_files)} Python code examples...\n")

    total_errors = 0
    failed_files = []

    for py_file in python_files:
        relative_path = py_file.relative_to(code_examples_dir)
        errors = validate_example(py_file)

        if errors:
            print(f"❌ {relative_path}")
            for error in errors:
                print(f"   - {error}")
            total_errors += len(errors)
            failed_files.append(str(relative_path))
        else:
            print(f"✅ {relative_path}")

    print(f"\n{'='*60}")
    print(f"Validation complete:")
    print(f"  Total files: {len(python_files)}")
    print(f"  Passed: {len(python_files) - len(failed_files)}")
    print(f"  Failed: {len(failed_files)}")
    print(f"  Total errors: {total_errors}")

    if failed_files:
        print(f"\nFailed files:")
        for f in failed_files:
            print(f"  - {f}")
        return 1

    return 0

if __name__ == '__main__':
    sys.exit(main())
