import subprocess
import sys

def test_age_validator():
    """Test exercise8_age_validator.py"""
    # Test child
    result = subprocess.run(['python3', 'exercise8_age_validator.py'],
                          input="10\n",
                          capture_output=True, text=True)
    assert "child" in result.stdout.lower(), "Should detect child"
    
    # Test teenager
    result = subprocess.run(['python3', 'exercise8_age_validator.py'],
                          input="15\n",
                          capture_output=True, text=True)
    assert "teenager" in result.stdout.lower(), "Should detect teenager"
    
    # Test adult
    result = subprocess.run(['python3', 'exercise8_age_validator.py'],
                          input="30\n",
                          capture_output=True, text=True)
    assert "adult" in result.stdout.lower(), "Should detect adult"
    
    # Test senior
    result = subprocess.run(['python3', 'exercise8_age_validator.py'],
                          input="70\n",
                          capture_output=True, text=True)
    assert "senior" in result.stdout.lower(), "Should detect senior"
    
    # Test invalid input
    result = subprocess.run(['python3', 'exercise8_age_validator.py'],
                          input="not a number\n",
                          capture_output=True, text=True)
    assert "valid" in result.stdout.lower() or "number" in result.stdout.lower(), "Should handle invalid input"
    
    print("✓ Age validator project passed!")

if __name__ == "__main__":
    try:
        test_age_validator()
        print("\n✓ Project exercise passed!")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
