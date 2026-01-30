import subprocess
import sys

def test_fizzbuzz():
    """Test exercise8_fizzbuzz.py"""
    result = subprocess.run(['python3', 'exercise8_fizzbuzz.py'], 
                          capture_output=True, text=True)
    
    lines = result.stdout.strip().split('\n')
    
    # Verify length (should be 100 lines)
    assert len(lines) == 100, f"Should have 100 lines, got {len(lines)}"
    
    # Check specific cases
    assert lines[0] == "1", "Line 1 should be '1'"
    assert lines[1] == "2", "Line 2 should be '2'"
    assert lines[2] == "Fizz", "Line 3 should be 'Fizz'"
    assert lines[3] == "4", "Line 4 should be '4'"
    assert lines[4] == "Buzz", "Line 5 should be 'Buzz'"
    assert lines[5] == "Fizz", "Line 6 should be 'Fizz'"
    assert lines[14] == "FizzBuzz", "Line 15 should be 'FizzBuzz'"
    assert lines[29] == "FizzBuzz", "Line 30 should be 'FizzBuzz'"
    
    print("✓ FizzBuzz project passed!")

if __name__ == "__main__":
    try:
        test_fizzbuzz()
        print("\n✓ Project exercise passed!")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
