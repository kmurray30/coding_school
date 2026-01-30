import subprocess
import sys

def test_exercise1():
    """Test exercise1_comparisons.py"""
    result = subprocess.run(['python3', 'exercise1_comparisons.py'], 
                          capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    assert lines[0] == "True"
    assert lines[1] == "False"
    assert lines[2] == "True"
    assert lines[3] == "True"
    assert lines[4] == "True"
    assert lines[5] == "False"
    print("✓ Exercise 1 passed")

def test_exercise2():
    """Test exercise2_string_comparison.py"""
    result = subprocess.run(['python3', 'exercise2_string_comparison.py'], 
                          capture_output=True, text=True)
    assert "True" in result.stdout
    assert "False" in result.stdout
    print("✓ Exercise 2 passed")

def test_exercise3():
    """Test exercise3_logical_and.py"""
    result = subprocess.run(['python3', 'exercise3_logical_and.py'], 
                          capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    assert lines[0] == "True"
    assert lines[1] == "False"
    print("✓ Exercise 3 passed")

def test_exercise4():
    """Test exercise4_logical_or.py"""
    result = subprocess.run(['python3', 'exercise4_logical_or.py'], 
                          capture_output=True, text=True)
    assert "True" in result.stdout
    assert "False" in result.stdout
    print("✓ Exercise 4 passed")

def test_exercise5():
    """Test exercise5_logical_not.py"""
    result = subprocess.run(['python3', 'exercise5_logical_not.py'], 
                          capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    assert lines[0] == "False"
    assert lines[1] == "True"
    assert lines[2] == "True"
    print("✓ Exercise 5 passed")

def test_exercise6():
    """Test exercise6_basic_if.py"""
    result = subprocess.run(['python3', 'exercise6_basic_if.py'], 
                          capture_output=True, text=True)
    assert "You can vote" in result.stdout
    print("✓ Exercise 6 passed")

def test_exercise7():
    """Test exercise7_if_else_elif.py"""
    result = subprocess.run(['python3', 'exercise7_if_else_elif.py'], 
                          capture_output=True, text=True)
    assert "Grade: B" in result.stdout
    print("✓ Exercise 7 passed")

if __name__ == "__main__":
    try:
        test_exercise1()
        test_exercise2()
        test_exercise3()
        test_exercise4()
        test_exercise5()
        test_exercise6()
        test_exercise7()
        print("\n✓ All auto-gradable exercises passed!")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
