import subprocess
import sys

def test_exercise1():
    """Test exercise1_local_scope.py"""
    result = subprocess.run(['python3', 'exercise1_local_scope.py'], 
                          capture_output=True, text=True)
    assert "I'm local" in result.stdout
    assert result.returncode == 0
    print("✓ Exercise 1 passed")

def test_exercise2():
    """Test exercise2_global_scope.py"""
    result = subprocess.run(['python3', 'exercise2_global_scope.py'], 
                          capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    assert lines[0] == "I'm global"
    assert lines[1] == "I'm global"
    print("✓ Exercise 2 passed")

def test_exercise3():
    """Test exercise3_shadowing.py"""
    result = subprocess.run(['python3', 'exercise3_shadowing.py'], 
                          capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    assert lines[0] == "Local Name"
    assert lines[1] == "Global Name"
    print("✓ Exercise 3 passed")

def test_exercise4():
    """Test exercise4_modify_global.py"""
    result = subprocess.run(['python3', 'exercise4_modify_global.py'], 
                          capture_output=True, text=True)
    assert "Before: 0" in result.stdout
    assert "After: 1" in result.stdout
    assert "After again: 2" in result.stdout
    print("✓ Exercise 4 passed")

def test_exercise5():
    """Test exercise5_return_not_global.py"""
    result = subprocess.run(['python3', 'exercise5_return_not_global.py'], 
                          capture_output=True, text=True)
    assert "8" in result.stdout
    assert "28" in result.stdout
    print("✓ Exercise 5 passed")

def test_exercise6():
    """Test exercise6_nested_scope.py"""
    result = subprocess.run(['python3', 'exercise6_nested_scope.py'], 
                          capture_output=True, text=True)
    assert "From outer" in result.stdout
    print("✓ Exercise 6 passed")

if __name__ == "__main__":
    try:
        test_exercise1()
        test_exercise2()
        test_exercise3()
        test_exercise4()
        test_exercise5()
        test_exercise6()
        print("\n✓ All auto-gradable exercises passed!")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
