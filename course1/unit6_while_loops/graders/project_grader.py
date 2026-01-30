import subprocess
import sys

def test_guessing_game():
    """Test exercise8_guessing_game.py - verify it runs and handles guesses"""
    # We can't test exact behavior since number is random
    # But we can test with programmatic input
    test_input = "50\n75\n90\n95\n100\n"
    
    result = subprocess.run(['python3', 'exercise8_guessing_game.py'],
                          input=test_input,
                          capture_output=True, text=True,
                          timeout=5)
    
    # Check it prompts for guesses
    assert "guess" in result.stdout.lower(), "Should prompt for guesses"
    
    # Check it gives feedback (Higher or Lower)
    has_feedback = "higher" in result.stdout.lower() or "lower" in result.stdout.lower()
    assert has_feedback, "Should give Higher/Lower feedback"
    
    # The game should either complete or show multiple prompts
    assert result.returncode == 0 or result.stdout.count("guess") > 1
    
    print("✓ Guessing game project passed!")

if __name__ == "__main__":
    try:
        test_guessing_game()
        print("\n✓ Project exercise passed!")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
