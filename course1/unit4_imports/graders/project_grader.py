import subprocess
import sys

def test_dice_roller():
    """Test exercise7_dice_roller.py"""
    # Test rolling 2 six-sided dice
    test_input = "2\n6\n"
    result = subprocess.run(['python3', 'exercise7_dice_roller.py'],
                          input=test_input,
                          capture_output=True, text=True)
    
    # Check prompts
    assert "dice" in result.stdout.lower(), "Should prompt for number of dice"
    assert "sides" in result.stdout.lower(), "Should prompt for number of sides"
    
    # Check rolled messages (should be 2 of them)
    assert result.stdout.count("Rolled:") == 2, "Should show 2 dice rolls"
    
    # Check total is shown
    assert "Total:" in result.stdout, "Should show total"
    
    print("✓ Dice roller project passed!")

if __name__ == "__main__":
    try:
        test_dice_roller()
        print("\n✓ Project exercise passed!")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
