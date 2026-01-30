import subprocess
import sys

def test_exercise1():
    """Test exercise1_simple_while.py"""
    result = subprocess.run(['python3', 'exercise1_simple_while.py'], 
                          capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    assert lines == ['1', '2', '3', '4', '5']
    print("✓ Exercise 1 passed")

def test_exercise2():
    """Test exercise2_countdown.py"""
    result = subprocess.run(['python3', 'exercise2_countdown.py'], 
                          capture_output=True, text=True)
    assert "5" in result.stdout
    assert "4" in result.stdout
    assert "3" in result.stdout
    assert "2" in result.stdout
    assert "1" in result.stdout
    assert "Liftoff!" in result.stdout
    print("✓ Exercise 2 passed")

def test_exercise4():
    """Test exercise4_accumulator.py"""
    result = subprocess.run(['python3', 'exercise4_accumulator.py'], 
                          capture_output=True, text=True)
    assert "55" in result.stdout
    print("✓ Exercise 4 passed")

def test_exercise5():
    """Test exercise5_break.py"""
    result = subprocess.run(['python3', 'exercise5_break.py'], 
                          capture_output=True, text=True)
    assert "1" in result.stdout
    assert "5" in result.stdout
    assert "Done!" in result.stdout
    print("✓ Exercise 5 passed")

def test_exercise6():
    """Test exercise6_continue.py"""
    result = subprocess.run(['python3', 'exercise6_continue.py'], 
                          capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    # Should only print odd numbers
    assert '1' in lines
    assert '3' in lines
    assert '5' in lines
    assert '7' in lines
    assert '9' in lines
    assert '2' not in result.stdout
    print("✓ Exercise 6 passed")

# Exercises 3, 7 use input() - self-check only

if __name__ == "__main__":
    try:
        test_exercise1()
        test_exercise2()
        test_exercise4()
        test_exercise5()
        test_exercise6()
        print("\n✓ All auto-gradable exercises passed!")
        print("\nExercises 3, 7 use input() - validate by running them yourself.")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
