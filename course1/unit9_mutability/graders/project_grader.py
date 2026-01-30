import subprocess
import sys

def test_shared_state_bug():
    """Test exercise8_shared_state_bug.py - verify fix works"""
    result = subprocess.run(['python3', 'exercise8_shared_state_bug.py'], 
                          capture_output=True, text=True)
    
    # Should show independent lists
    assert "List 1: ['apples']" in result.stdout
    assert "List 2: ['bananas']" in result.stdout
    
    # list2 should NOT contain apples
    lines = result.stdout.strip().split('\n')
    list2_line = [line for line in lines if "List 2:" in line][0]
    assert "apples" not in list2_line, "List 2 should not contain apples"
    
    print("✓ Shared state bug fix passed!")

if __name__ == "__main__":
    try:
        test_shared_state_bug()
        print("\n✓ Project exercise passed!")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
