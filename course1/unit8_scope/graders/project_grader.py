import subprocess
import sys

def test_refactor():
    """Test exercise7_refactor_globals.py - should output 15"""
    result = subprocess.run(['python3', 'exercise7_refactor_globals.py'], 
                          capture_output=True, text=True)
    
    assert "15" in result.stdout, "Should calculate total as 15"
    assert result.returncode == 0, "Should run without errors"
    
    print("✓ Refactoring project passed!")

if __name__ == "__main__":
    try:
        test_refactor()
        print("\n✓ Project exercise passed!")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
