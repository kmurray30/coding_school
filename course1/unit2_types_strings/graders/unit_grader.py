import subprocess
import sys

def test_exercise1():
    """Test exercise1_strings.py"""
    result = subprocess.run(['python3', 'exercise1_strings.py'], 
                          capture_output=True, text=True)
    assert "Primeagen" in result.stdout
    assert "Single quotes work too" in result.stdout
    print("✓ Exercise 1 passed")

def test_exercise2():
    """Test exercise2_ints.py"""
    result = subprocess.run(['python3', 'exercise2_ints.py'], 
                          capture_output=True, text=True)
    assert "10000" in result.stdout
    assert "25" in result.stdout
    assert "10025" in result.stdout
    print("✓ Exercise 2 passed")

def test_exercise3():
    """Test exercise3_math_ops.py"""
    result = subprocess.run(['python3', 'exercise3_math_ops.py'], 
                          capture_output=True, text=True)
    assert "15" in result.stdout
    assert "5" in result.stdout
    assert "50" in result.stdout
    assert "2.0" in result.stdout
    print("✓ Exercise 3 passed")

def test_exercise4():
    """Test exercise4_type_function.py"""
    result = subprocess.run(['python3', 'exercise4_type_function.py'], 
                          capture_output=True, text=True)
    assert "'str'" in result.stdout
    assert "'int'" in result.stdout
    assert "'float'" in result.stdout
    assert "'bool'" in result.stdout
    print("✓ Exercise 4 passed")

def test_exercise5():
    """Test exercise5_floats.py"""
    result = subprocess.run(['python3', 'exercise5_floats.py'], 
                          capture_output=True, text=True)
    assert "1.5992" in result.stdout
    print("✓ Exercise 5 passed")

def test_exercise6():
    """Test exercise6_casting.py"""
    result = subprocess.run(['python3', 'exercise6_casting.py'], 
                          capture_output=True, text=True)
    assert "50" in result.stdout
    assert "I am 25" in result.stdout
    print("✓ Exercise 6 passed")

def test_exercise7():
    """Test exercise7_cast_error.py"""
    result = subprocess.run(['python3', 'exercise7_cast_error.py'], 
                          capture_output=True, text=True)
    assert "123" in result.stdout
    assert result.returncode == 0
    print("✓ Exercise 7 passed")

def test_exercise8():
    """Test exercise8_float_to_int.py"""
    result = subprocess.run(['python3', 'exercise8_float_to_int.py'], 
                          capture_output=True, text=True)
    assert "9" in result.stdout
    print("✓ Exercise 8 passed")

def test_exercise9():
    """Test exercise9_string_concat.py"""
    result = subprocess.run(['python3', 'exercise9_string_concat.py'], 
                          capture_output=True, text=True)
    assert "Primeagen" in result.stdout
    print("✓ Exercise 9 passed")

def test_exercise10():
    """Test exercise10_booleans.py"""
    result = subprocess.run(['python3', 'exercise10_booleans.py'], 
                          capture_output=True, text=True)
    assert "True" in result.stdout
    assert "False" in result.stdout
    assert "'bool'" in result.stdout
    print("✓ Exercise 10 passed")

if __name__ == "__main__":
    try:
        test_exercise1()
        test_exercise2()
        test_exercise3()
        test_exercise4()
        test_exercise5()
        test_exercise6()
        test_exercise7()
        test_exercise8()
        test_exercise9()
        test_exercise10()
        print("\n✓ All unit exercises passed!")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
