#!/usr/bin/env python3
"""
Test file for greeting.py

This file tests your greeting functions to make sure they format strings correctly.
Run this file to check your work!

Usage:
    python tests/test_greeting.py

WHAT YOU'RE LEARNING:
- How to test string functions
- Why exact formatting matters (spaces, punctuation)
- How automated tests check your code
"""

import sys
import os

# Add the parent directory to the path so we can import from exercises
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from exercises.greeting import *


def test_greeting():
    """
    Run all greeting tests.

    Tests each greeting function to ensure proper string formatting.
    """
    print("\n" + "=" * 70)
    print(" GREETING TESTS - Basic Test Suite")
    print("=" * 70 + "\n")

    errors = []

    # Test 1: create_greeting
    print("[Test 1/5] Testing basic greeting...")
    try:
        result = create_greeting("Alice")
        expected = "Hello, Alice!"
        if result != expected:
            errors.append(f"create_greeting failed: got '{result}', expected '{expected}'")
            print(f"  ✗ FAIL: Expected '{expected}'")
            print(f"          Got      '{result}'")
        else:
            print("  ✓ PASS: Basic greeting works correctly")
    except Exception as e:
        errors.append(f"create_greeting crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test 2: create_goodbye
    print("[Test 2/5] Testing goodbye message...")
    try:
        result = create_goodbye("Bob")
        expected = "Goodbye, Bob!"
        if result != expected:
            errors.append(f"create_goodbye failed: got '{result}', expected '{expected}'")
            print(f"  ✗ FAIL: Expected '{expected}'")
            print(f"          Got      '{result}'")
        else:
            print("  ✓ PASS: Goodbye message works correctly")
    except Exception as e:
        errors.append(f"create_goodbye crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test 3: create_introduction
    print("[Test 3/5] Testing introduction with age...")
    try:
        result = create_introduction("Charlie", 25)
        expected = "My name is Charlie and I am 25 years old."
        if result != expected:
            errors.append(f"create_introduction failed: check string formatting and str() conversion")
            print(f"  ✗ FAIL: Expected '{expected}'")
            print(f"          Got      '{result}'")
        else:
            print("  ✓ PASS: Introduction works correctly")
    except Exception as e:
        errors.append(f"create_introduction crashed: {e}")
        print(f"  ✗ ERROR: {e}")
        if "can only concatenate str" in str(e):
            print("  💡 HINT: Did you forget to use str() to convert age to a string?")
    print()

    # Test 4: create_welcome_message
    print("[Test 4/5] Testing welcome message...")
    try:
        result = create_welcome_message("Diana", "Mumbai")
        expected = "Welcome Diana from Mumbai!"
        if result != expected:
            errors.append(f"create_welcome_message failed: check spacing between words")
            print(f"  ✗ FAIL: Expected '{expected}'")
            print(f"          Got      '{result}'")
            if " " not in result or result.count(" ") < 3:
                print("  💡 HINT: Don't forget spaces between words!")
        else:
            print("  ✓ PASS: Welcome message works correctly")
    except Exception as e:
        errors.append(f"create_welcome_message crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test 5: create_full_greeting
    print("[Test 5/5] Testing full greeting...")
    try:
        result = create_full_greeting("Eve", 30, "Delhi")
        expected = "Hello Eve! You are 30 years old and from Delhi."
        if result != expected:
            errors.append(f"create_full_greeting failed: check string formatting")
            print(f"  ✗ FAIL: Expected '{expected}'")
            print(f"          Got      '{result}'")
        else:
            print("  ✓ PASS: Full greeting works correctly")
    except Exception as e:
        errors.append(f"create_full_greeting crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Print summary
    print("=" * 70)
    if errors:
        print(" TESTS FAILED ❌")
        print("=" * 70)
        print("\nErrors found:")
        for i, error in enumerate(errors, 1):
            print(f"  {i}. {error}")
        print("\n💡 TIPS:")
        print("  - Check for proper spacing between words")
        print("  - Make sure punctuation is correct (commas, periods, exclamation marks)")
        print("  - Remember to use str() to convert numbers to strings")
        print("  - Compare your output carefully with the expected output")
        return False
    else:
        print(" ALL TESTS PASSED! ✅")
        print("=" * 70)
        print("\n🎉 Excellent! Your greeting functions work correctly!")
        print("📝 Don't forget to commit your changes:")
        print("   git add exercises/greeting.py")
        print('   git commit -m "Complete greeting functions"')
        return True


if __name__ == "__main__":
    success = test_greeting()
    # Exit with appropriate code for automated testing
    exit(0 if success else 1)
