#!/usr/bin/env python3
"""
Unit 2 Project Grader - Tests exercise 8 (multi-file project)

This validates the greeting_app project structure and files.
"""

import subprocess
import sys
import os

def check_file_exists(filepath):
    """Check if a file exists"""
    return os.path.exists(filepath)

def run_python_file(filepath):
    """Run a Python file and capture output"""
    try:
        result = subprocess.run(
            ['python3', filepath],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired:
        return "", "Timeout: File took too long to run", 1
    except Exception as error:
        return "", f"Error running file: {error}", 1

def test_greeting_app_structure():
    """Test that greeting_app directory and files exist"""
    print("Testing Exercise 8: Multi-file Python project...")
    print()
    
    # Try to find greeting_app in common locations
    possible_locations = [
        '../../../greeting_app',  # Same level as course0
        '../../greeting_app',      # Parent of unit2
        '../greeting_app',         # Next to graders
        'greeting_app',            # Current directory
        os.path.expanduser('~/greeting_app'),  # Home directory
        os.path.expanduser('~/Desktop/greeting_app'),  # Desktop
    ]
    
    greeting_app_path = None
    for location in possible_locations:
        if os.path.isdir(location):
            greeting_app_path = location
            print(f"✓ Found greeting_app at: {os.path.abspath(location)}")
            break
    
    if not greeting_app_path:
        print("✗ greeting_app directory not found")
        print("\nSearched in:")
        for location in possible_locations:
            print(f"  - {os.path.abspath(location)}")
        print("\nCreate the greeting_app directory and try again.")
        return False
    
    # Check for the three Python files
    required_files = {
        'greeting1.py': 'Hello from file 1!',
        'greeting2.py': 'Greetings from file 2!',
        'greeting3.py': 'Salutations from file 3!',
    }
    
    all_passed = True
    
    for filename, expected_output in required_files.items():
        filepath = os.path.join(greeting_app_path, filename)
        
        # Check if file exists
        if not check_file_exists(filepath):
            print(f"✗ {filename} not found")
            all_passed = False
            continue
        
        print(f"✓ {filename} exists")
        
        # Run the file and check output
        stdout, stderr, returncode = run_python_file(filepath)
        
        if returncode != 0:
            print(f"  ✗ {filename} had errors:\n{stderr}")
            all_passed = False
            continue
        
        if expected_output not in stdout:
            print(f"  ✗ {filename} output incorrect")
            print(f"     Expected: {expected_output}")
            print(f"     Got: {stdout.strip()}")
            all_passed = False
            continue
        
        print(f"  ✓ {filename} produces correct output")
    
    return all_passed

def main():
    """Run project grader"""
    print("=" * 60)
    print("Unit 2 Project Grader - Multi-file Python Project")
    print("=" * 60)
    print()
    
    success = test_greeting_app_structure()
    
    print()
    print("=" * 60)
    
    if success:
        print("🎉 Project passed! You've got the Python workflow down.")
        print("\nYou can now:")
        print("- Navigate directories with the terminal")
        print("- Use VSCode to create and edit files")
        print("- Create and run Python files")
        print("- Manage multi-file projects")
        print("\nTake the Unit 2 quiz, then move on to the final exam!")
        return 0
    else:
        print("Project needs work. Review the failures above.")
        print("\nMake sure you:")
        print("1. Created a directory called 'greeting_app'")
        print("2. Created greeting1.py, greeting2.py, greeting3.py inside it")
        print("3. Each file has the correct print() statement")
        return 1

if __name__ == "__main__":
    sys.exit(main())
