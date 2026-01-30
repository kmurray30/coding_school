import subprocess
import sys

def test_exercise1():
    """Test exercise1_immutable_strings.py"""
    result = subprocess.run(['python3', 'exercise1_immutable_strings.py'], 
                          capture_output=True, text=True)
    assert "primeagen" in result.stdout
    assert result.returncode == 0
    print("✓ Exercise 1 passed")

def test_exercise2():
    """Test exercise2_mutable_lists.py"""
    result = subprocess.run(['python3', 'exercise2_mutable_lists.py'], 
                          capture_output=True, text=True)
    assert "[1, 2, 3, 4, 5]" in result.stdout
    assert "[100, 2, 3, 4, 5]" in result.stdout
    print("✓ Exercise 2 passed")

def test_exercise3():
    """Test exercise3_list_methods.py"""
    result = subprocess.run(['python3', 'exercise3_list_methods.py'], 
                          capture_output=True, text=True)
    assert "['apple', 'banana']" in result.stdout
    assert "['apple', 'banana', 'orange']" in result.stdout
    assert "['apple', 'orange']" in result.stdout
    assert "Popped: orange" in result.stdout
    assert "['apple']" in result.stdout
    print("✓ Exercise 3 passed")

def test_exercise4():
    """Test exercise4_list_vs_tuple.py"""
    result = subprocess.run(['python3', 'exercise4_list_vs_tuple.py'], 
                          capture_output=True, text=True)
    assert "[100, 2, 3]" in result.stdout
    assert "(100, 2, 3)" in result.stdout
    print("✓ Exercise 4 passed")

def test_exercise5():
    """Test exercise5_reference_behavior.py"""
    result = subprocess.run(['python3', 'exercise5_reference_behavior.py'], 
                          capture_output=True, text=True)
    # Both lists should show [1, 2, 3, 4] after modification
    assert result.stdout.count("[1, 2, 3, 4]") >= 2
    print("✓ Exercise 5 passed")

def test_exercise6():
    """Test exercise6_copying_lists.py"""
    result = subprocess.run(['python3', 'exercise6_copying_lists.py'], 
                          capture_output=True, text=True)
    # list1 should have 4, list2 should not
    assert "[1, 2, 3, 4]" in result.stdout
    assert result.stdout.count("[1, 2, 3]") >= 1
    print("✓ Exercise 6 passed")

def test_exercise7():
    """Test exercise7_dict_mutability.py"""
    result = subprocess.run(['python3', 'exercise7_dict_mutability.py'], 
                          capture_output=True, text=True)
    assert "'age': 30" in result.stdout
    assert "'age': 31" in result.stdout
    assert "'language': 'Rust'" in result.stdout
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
