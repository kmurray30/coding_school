import subprocess
import sys

def test_calculator():
    """Test exercise8_calculator.py"""
    # Test addition
    test_input = "10\n5\nadd\n"
    result = subprocess.run(['python3', 'exercise8_calculator.py'],
                          input=test_input,
                          capture_output=True, text=True)
    assert "15" in result.stdout, "Addition should work"
    
    # Test multiplication
    test_input = "10\n5\nmultiply\n"
    result = subprocess.run(['python3', 'exercise8_calculator.py'],
                          input=test_input,
                          capture_output=True, text=True)
    assert "50" in result.stdout, "Multiplication should work"
    
    print("✓ Calculator project passed!")

if __name__ == "__main__":
    try:
        test_calculator()
        print("\n✓ Project exercise passed!")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
