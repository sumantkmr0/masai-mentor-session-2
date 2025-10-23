#!/usr/bin/env python3
"""
HIDDEN TEST FILE - Advanced Greeting Tests

These tests check edge cases with different names and formats.
Students will see these when they create a pull request!

This teaches:
- Handling various string inputs
- Consistency in string formatting
- Importance of exact output matching
"""

import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from exercises.greeting import *


def test_greeting_advanced():
    """
    Run advanced greeting tests with edge cases.
    """
    print("\n" + "=" * 70)
    print(" HIDDEN TESTS - Greeting Edge Cases 🔍")
    print("=" * 70)
    print("\nSurprise! These test your functions with various inputs!\n")

    errors = []

    # Test with single letter names
    print("[Hidden Test 1] Testing with short names...")
    try:
        result = create_greeting("A")
        expected = "Hello, A!"
        if result != expected:
            errors.append(f"create_greeting('A') failed: got '{result}'")
            print(f"  ✗ FAIL: Expected '{expected}', got '{result}'")
        else:
            print("  ✓ PASS: Works with single letter names!")
    except Exception as e:
        errors.append(f"Short name test crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test with long names
    print("[Hidden Test 2] Testing with long names...")
    try:
        result = create_goodbye("Srinivasa Ramanujan")
        expected = "Goodbye, Srinivasa Ramanujan!"
        if result != expected:
            errors.append(f"create_goodbye with long name failed")
            print(f"  ✗ FAIL: Expected '{expected}'")
            print(f"          Got      '{result}'")
        else:
            print("  ✓ PASS: Works with long names!")
    except Exception as e:
        errors.append(f"Long name test crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test with different ages
    print("[Hidden Test 3] Testing with various ages...")
    try:
        result1 = create_introduction("Baby", 1)
        expected1 = "My name is Baby and I am 1 years old."
        result2 = create_introduction("Elder", 100)
        expected2 = "My name is Elder and I am 100 years old."

        if result1 != expected1:
            errors.append(f"create_introduction with age 1 failed")
            print(f"  ✗ FAIL: Age 1 - Expected '{expected1}'")
            print(f"          Got      '{result1}'")
        elif result2 != expected2:
            errors.append(f"create_introduction with age 100 failed")
            print(f"  ✗ FAIL: Age 100 - Expected '{expected2}'")
            print(f"          Got      '{result2}'")
        else:
            print("  ✓ PASS: Works with various ages!")
    except Exception as e:
        errors.append(f"Age variation test crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test welcome message with different cities
    print("[Hidden Test 4] Testing with various cities...")
    try:
        result = create_welcome_message("Raj", "New Delhi")
        expected = "Welcome Raj from New Delhi!"
        if result != expected:
            errors.append(f"create_welcome_message with multi-word city failed")
            print(f"  ✗ FAIL: Expected '{expected}'")
            print(f"          Got      '{result}'")
        else:
            print("  ✓ PASS: Works with multi-word city names!")
    except Exception as e:
        errors.append(f"City variation test crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test full greeting with various inputs
    print("[Hidden Test 5] Testing full greeting with edge cases...")
    try:
        result = create_full_greeting("Sam", 18, "Bangalore")
        expected = "Hello Sam! You are 18 years old and from Bangalore."
        if result != expected:
            errors.append(f"create_full_greeting edge case failed")
            print(f"  ✗ FAIL: Expected '{expected}'")
            print(f"          Got      '{result}'")
        else:
            print("  ✓ PASS: Full greeting handles all cases!")
    except Exception as e:
        errors.append(f"Full greeting test crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test consistency
    print("[Hidden Test 6] Testing output consistency...")
    try:
        # Run same function multiple times
        results = [create_greeting("Test") for _ in range(3)]
        if len(set(results)) != 1:
            errors.append("create_greeting returns inconsistent results")
            print("  ✗ FAIL: Function returns different results for same input")
        else:
            print("  ✓ PASS: Functions are consistent!")
    except Exception as e:
        errors.append(f"Consistency test crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Print summary
    print("=" * 70)
    if errors:
        print(" SOME HIDDEN TESTS FAILED ⚠️")
        print("=" * 70)
        print(f"\nFound {len(errors)} issues in edge cases:")
        for i, error in enumerate(errors, 1):
            print(f"  {i}. {error}")
        print("\n💡 Your basic functionality works!")
        print("   These tests help ensure your code works in all scenarios.")
        return False
    else:
        print(" ALL HIDDEN TESTS PASSED! 🌟")
        print("=" * 70)
        print("\n🎉 Amazing! Your greeting functions are perfect!")
        print("   They handle all edge cases correctly!")
        return True


if __name__ == "__main__":
    success = test_greeting_advanced()
    exit(0 if success else 1)
