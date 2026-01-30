import subprocess
import sys

def test_string_builder():
    """Test exercise11_string_builder.py"""
    test_input = "Alice\n25\nNew York\n"
    
    result = subprocess.run(['python3', 'exercise11_string_builder.py'],
                          input=test_input,
                          capture_output=True, text=True)
    
    # Check prompts
    assert "name" in result.stdout.lower()
    assert "age" in result.stdout.lower()
    assert "city" in result.stdout.lower()
    
    # Check bio construction
    assert "Alice" in result.stdout
    assert "25" in result.stdout
    assert "New York" in result.stdout
    
    # Check adult boolean
    assert "Adult: True" in result.stdout or "Adult: False" in result.stdout
    
    print("✓ String builder project passed!")

if __name__ == "__main__":
    try:
        test_string_builder()
        print("\n✓ Project exercise passed!")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
