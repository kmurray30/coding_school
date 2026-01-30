import subprocess
import sys

def test_exercise1():
    """Test exercise1_range_basic.py"""
    result = subprocess.run(['python3', 'exercise1_range_basic.py'], 
                          capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    assert lines == ['0', '1', '2', '3', '4']
    print("✓ Exercise 1 passed")

def test_exercise2():
    """Test exercise2_range_params.py"""
    result = subprocess.run(['python3', 'exercise2_range_params.py'], 
                          capture_output=True, text=True)
    assert "1" in result.stdout
    assert "9" in result.stdout
    assert "0" in result.stdout
    assert "2" in result.stdout
    assert "4" in result.stdout
    assert "6" in result.stdout
    assert "8" in result.stdout
    print("✓ Exercise 2 passed")

def test_exercise3():
    """Test exercise3_iterate_string.py"""
    result = subprocess.run(['python3', 'exercise3_iterate_string.py'], 
                          capture_output=True, text=True)
    assert "P" in result.stdout
    assert "r" in result.stdout
    assert "i" in result.stdout
    print("✓ Exercise 3 passed")

def test_exercise4():
    """Test exercise4_list_iteration.py"""
    result = subprocess.run(['python3', 'exercise4_list_iteration.py'], 
                          capture_output=True, text=True)
    assert "I like pizza" in result.stdout
    assert "I like tacos" in result.stdout
    assert "I like burgers" in result.stdout
    print("✓ Exercise 4 passed")

def test_exercise5():
    """Test exercise5_accumulator.py"""
    result = subprocess.run(['python3', 'exercise5_accumulator.py'], 
                          capture_output=True, text=True)
    assert "Sum of 1-10: 55" in result.stdout
    assert "Product of 1-5: 120" in result.stdout
    print("✓ Exercise 5 passed")

def test_exercise6():
    """Test exercise6_nested_loops.py"""
    result = subprocess.run(['python3', 'exercise6_nested_loops.py'], 
                          capture_output=True, text=True)
    assert "1 x 1 = 1" in result.stdout
    assert "2 x 2 = 4" in result.stdout
    assert "3 x 3 = 9" in result.stdout
    print("✓ Exercise 6 passed")

def test_exercise7():
    """Test exercise7_pattern_printing.py"""
    result = subprocess.run(['python3', 'exercise7_pattern_printing.py'], 
                          capture_output=True, text=True)
    assert "*" in result.stdout
    assert "**" in result.stdout
    assert "*****" in result.stdout
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
        print("\n✓ All unit exercises passed!")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
