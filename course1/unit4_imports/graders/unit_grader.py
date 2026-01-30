import subprocess
import sys

def test_exercise1():
    """Test exercise1_import_math.py"""
    result = subprocess.run(['python3', 'exercise1_import_math.py'], 
                          capture_output=True, text=True)
    assert "4.0" in result.stdout
    assert "8.0" in result.stdout
    print("✓ Exercise 1 passed")

def test_exercise2():
    """Test exercise2_from_import.py"""
    result = subprocess.run(['python3', 'exercise2_from_import.py'], 
                          capture_output=True, text=True)
    assert "3.14159" in result.stdout
    assert "6.28318" in result.stdout
    print("✓ Exercise 2 passed")

def test_exercise3():
    """Test exercise3_multiple_imports.py"""
    result = subprocess.run(['python3', 'exercise3_multiple_imports.py'], 
                          capture_output=True, text=True)
    assert "5.0" in result.stdout
    assert "3.14159" in result.stdout
    assert "5" in result.stdout
    print("✓ Exercise 3 passed")

def test_exercise4():
    """Test exercise4_random.py - just verify it runs"""
    result = subprocess.run(['python3', 'exercise4_random.py'], 
                          capture_output=True, text=True)
    assert result.returncode == 0, "Should run without errors"
    lines = result.stdout.strip().split('\n')
    assert len(lines) >= 2, "Should print at least 2 random numbers"
    print("✓ Exercise 4 passed")

def test_exercise5():
    """Test exercise5_datetime.py - verify it runs and prints year"""
    result = subprocess.run(['python3', 'exercise5_datetime.py'], 
                          capture_output=True, text=True)
    assert result.returncode == 0, "Should run without errors"
    # Should print current year somewhere
    import datetime
    current_year = str(datetime.datetime.now().year)
    assert current_year in result.stdout, "Should print current year"
    print("✓ Exercise 5 passed")

# Exercise 6 is exploration - skip auto-grading

if __name__ == "__main__":
    try:
        test_exercise1()
        test_exercise2()
        test_exercise3()
        test_exercise4()
        test_exercise5()
        print("\n✓ All auto-gradable exercises passed!")
        print("\nExercise 6 is exploration - no auto-grading.")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
