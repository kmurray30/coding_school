#!/usr/bin/env python3
"""
Unit 2 Grader - Tests exercises 1-7

This grader validates that your Python files run correctly.
Students should already know they succeeded by running their code.
This is just confirmation.
"""

import subprocess
import sys
import os

def run_python_file(filename):
    """Run a Python file and capture output."""
    try:
        result = subprocess.run(
            ['python3', filename],
            capture_output=True,
            text=True,
            timeout=5,
            cwd=os.path.dirname(os.path.abspath(__file__)) + '/..'
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired:
        return "", "Timeout: File took too long to run", 1
    except Exception as error:
        return "", f"Error running file: {error}", 1

def test_exercise1():
    """Test exercise 1 - First Python file"""
    print("Testing Exercise 1: First Python file...")
    stdout, stderr, returncode = run_python_file('exercise1_first_py_file.py')
    
    if returncode != 0:
        print(f"  ✗ Failed - File had errors:\n{stderr}")
        return False
    
    if "Hello" not in stdout:
        print(f"  ✗ Failed - Expected 'Hello' in output, got: {stdout}")
        return False
    
    print("  ✓ Passed")
    return True

def test_exercise2():
    """Test exercise 2 - Run from terminal"""
    print("Testing Exercise 2: Run from terminal...")
    stdout, stderr, returncode = run_python_file('exercise2_run_from_terminal.py')
    
    if returncode != 0:
        print(f"  ✗ Failed - File had errors:\n{stderr}")
        return False
    
    if "This message came from the terminal" not in stdout:
        print(f"  ✗ Failed - Expected message not found in output: {stdout}")
        return False
    
    print("  ✓ Passed")
    return True

def test_exercise3():
    """Test exercise 3 - VSCode run button"""
    print("Testing Exercise 3: VSCode run button...")
    stdout, stderr, returncode = run_python_file('exercise3_vscode_run_button.py')
    
    if returncode != 0:
        print(f"  ✗ Failed - File had errors:\n{stderr}")
        return False
    
    if "This ran from VSCode's run button" not in stdout:
        print(f"  ✗ Failed - Expected message not found in output: {stdout}")
        return False
    
    print("  ✓ Passed")
    return True

def test_exercise4():
    """Test exercise 4 - Modify and rerun"""
    print("Testing Exercise 4: Modify and rerun...")
    stdout, stderr, returncode = run_python_file('exercise4_modify_and_rerun.py')
    
    if returncode != 0:
        print(f"  ✗ Failed - File had errors:\n{stderr}")
        return False
    
    # Just verify it runs and produces output
    if len(stdout.strip()) == 0:
        print(f"  ✗ Failed - No output produced")
        return False
    
    print("  ✓ Passed")
    return True

def test_exercise5():
    """Test exercise 5 - Multiple prints"""
    print("Testing Exercise 5: Multiple prints...")
    stdout, stderr, returncode = run_python_file('exercise5_multiple_prints.py')
    
    if returncode != 0:
        print(f"  ✗ Failed - File had errors:\n{stderr}")
        return False
    
    lines = stdout.strip().split('\n')
    if len(lines) < 3:
        print(f"  ✗ Failed - Expected at least 3 lines of output, got {len(lines)}")
        return False
    
    if "First message" not in stdout:
        print(f"  ✗ Failed - Expected 'First message' in output")
        return False
    
    if "Second message" not in stdout:
        print(f"  ✗ Failed - Expected 'Second message' in output")
        return False
        
    if "Third message" not in stdout:
        print(f"  ✗ Failed - Expected 'Third message' in output")
        return False
    
    print("  ✓ Passed")
    return True

def test_exercise6():
    """Test exercise 6 - Current directory matters"""
    print("Testing Exercise 6: Current directory matters...")
    stdout, stderr, returncode = run_python_file('exercise6_current_directory_matters.py')
    
    if returncode != 0:
        print(f"  ✗ Failed - File had errors:\n{stderr}")
        return False
    
    if "If you see this, you're in the right directory!" not in stdout:
        print(f"  ✗ Failed - Expected message not found in output: {stdout}")
        return False
    
    print("  ✓ Passed")
    return True

def test_exercise7():
    """Test exercise 7 - Syntax error (should be fixed by student)"""
    print("Testing Exercise 7: Syntax error...")
    stdout, stderr, returncode = run_python_file('exercise7_syntax_error.py')
    
    # This exercise should have an error initially, but student should fix it
    # We'll check if it's fixed (runs successfully)
    if returncode == 0:
        if "This will cause an error" in stdout:
            print("  ✓ Passed - Error was fixed!")
            return True
        else:
            print(f"  ✗ Failed - File runs but doesn't print expected message")
            return False
    else:
        print(f"  ⚠ Warning - File still has an error. Did you fix it?")
        print(f"  Error message: {stderr}")
        print(f"  Read the error message and fix the typo!")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("Unit 2 Grader - Python Files")
    print("=" * 60)
    print()
    
    tests = [
        test_exercise1,
        test_exercise2,
        test_exercise3,
        test_exercise4,
        test_exercise5,
        test_exercise6,
        test_exercise7,
    ]
    
    results = []
    for test_function in tests:
        results.append(test_function())
        print()
    
    # Summary
    passed = sum(results)
    total = len(results)
    
    print("=" * 60)
    print(f"Results: {passed}/{total} exercises passed")
    print("=" * 60)
    
    if passed == total:
        print("\n🎉 All exercises passed! Great work!")
        print("Move on to the quiz, then try the project grader.")
        return 0
    else:
        print(f"\n{total - passed} exercise(s) need work. Review the failures above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
