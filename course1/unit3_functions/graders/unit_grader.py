import subprocess
import sys

def test_exercise1():
    """Test exercise1_sequentiality.py"""
    result = subprocess.run(['python3', 'exercise1_sequentiality.py'], 
                          capture_output=True, text=True)
    assert "First" in result.stdout
    assert "Second" in result.stdout
    assert "Third" in result.stdout
    print("✓ Exercise 1 passed")

def test_exercise2():
    """Test exercise2_len_function.py"""
    result = subprocess.run(['python3', 'exercise2_len_function.py'], 
                          capture_output=True, text=True)
    assert "9" in result.stdout
    print("✓ Exercise 2 passed")

def test_exercise5():
    """Test exercise5_lowercase.py"""
    result = subprocess.run(['python3', 'exercise5_lowercase.py'], 
                          capture_output=True, text=True)
    assert "primeagen" in result.stdout
    assert "PRIMEAGEN" in result.stdout
    print("✓ Exercise 5 passed")

def test_exercise7():
    """Test exercise7_define_function.py"""
    result = subprocess.run(['python3', 'exercise7_define_function.py'], 
                          capture_output=True, text=True)
    assert "Hello Primeagen" in result.stdout
    assert "10" in result.stdout
    assert "200" in result.stdout
    print("✓ Exercise 7 passed")

# Exercises 3, 4, 6 use input() - self-check only

if __name__ == "__main__":
    try:
        test_exercise1()
        test_exercise2()
        test_exercise5()
        test_exercise7()
        print("\n✓ All auto-gradable exercises passed!")
        print("\nExercises 3, 4, 6 use input() - validate by running them yourself.")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
