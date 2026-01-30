import subprocess
import sys

def test_exercise1():
    """Test exercise1_hello.py - basic print"""
    result = subprocess.run(['python3', 'exercise1_hello.py'], 
                          capture_output=True, text=True)
    assert "Hello World!" in result.stdout, f"Expected 'Hello World!', got '{result.stdout}'"
    print("✓ Exercise 1 passed")

def test_exercise2():
    """Test exercise2_syntax.py - should run without syntax errors when fixed"""
    result = subprocess.run(['python3', 'exercise2_syntax.py'], 
                          capture_output=True, text=True)
    assert result.returncode == 0, f"Syntax errors remain: {result.stderr}"
    assert "Fix me!" in result.stdout, f"Expected 'Fix me!', got '{result.stdout}'"
    print("✓ Exercise 2 passed")

def test_exercise3():
    """Test exercise3_variables.py - variables and printing"""
    result = subprocess.run(['python3', 'exercise3_variables.py'], 
                          capture_output=True, text=True)
    assert "bananas" in result.stdout, f"Expected 'bananas' in output"
    assert "42" in result.stdout, f"Expected '42' in output"
    print("✓ Exercise 3 passed")

# Exercises 4-8 use input() so they're self-check only
# Students validate by running and comparing to expected output

if __name__ == "__main__":
    try:
        test_exercise1()
        test_exercise2()
        test_exercise3()
        print("\n✓ All auto-gradable exercises passed!")
        print("\nExercises 4-8 use input() - validate by running them yourself.")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
