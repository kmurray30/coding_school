import subprocess
import sys

def test_mad_libs():
    """Test exercise8_mad_libs.py - interactive Mad Libs"""
    # Provide test input
    test_input = "dragon\nfly\nmajestic\n"
    
    result = subprocess.run(['python3', 'exercise8_mad_libs.py'],
                          input=test_input,
                          capture_output=True, text=True)
    
    # Check that all three inputs are prompted for
    assert "noun" in result.stdout.lower(), "Should prompt for a noun"
    assert "verb" in result.stdout.lower(), "Should prompt for a verb"
    assert "adjective" in result.stdout.lower(), "Should prompt for an adjective"
    
    # Check that the story contains the user's words
    assert "dragon" in result.stdout.lower(), "Story should include the noun"
    assert "fly" in result.stdout.lower(), "Story should include the verb"
    assert "majestic" in result.stdout.lower(), "Story should include the adjective"
    
    print("✓ Mad Libs project passed!")

if __name__ == "__main__":
    try:
        test_mad_libs()
        print("\n✓ Project exercise passed!")
    except AssertionError as e:
        print(f"\n✗ Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
