#!/usr/bin/env python3
"""
Test file for calculator.py

This file contains basic tests that students can run locally.
Run this file to check if your calculator functions work correctly!

Usage:
    python tests/test_calculator.py

TESTING BEST PRACTICES:
- Always test your code before committing
- Read error messages carefully - they tell you what's wrong
- Fix one test at a time
- Run tests frequently as you code

This teaches you about automated testing - a crucial skill in software development!
"""

import sys
import os

# Add the parent directory to the path so we can import from exercises
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from exercises.calculator import *


def test_calculator():
    """
    Run all calculator tests.

    This function tests each calculator function and reports the results.
    Green checkmarks (✓) mean the test passed.
    Red X marks (✗) mean the test failed.
    """
    print("\n" + "=" * 70)
    print(" CALCULATOR TESTS - Basic Test Suite")
    print("=" * 70 + "\n")

    errors = []

    # Test 1: Addition
    print("[Test 1/6] Testing addition...")
    try:
        if add_numbers(5, 3) != 8:
            errors.append("❌ Addition failed: add_numbers(5, 3) should return 8")
            print("  ✗ FAIL: Expected 8, got", add_numbers(5, 3))
        else:
            print("  ✓ PASS: Addition works correctly")
    except Exception as e:
        errors.append(f"❌ Addition crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test 2: Subtraction
    print("[Test 2/6] Testing subtraction...")
    try:
        if subtract_numbers(10, 4) != 6:
            errors.append("❌ Subtraction failed: subtract_numbers(10, 4) should return 6")
            print("  ✗ FAIL: Expected 6, got", subtract_numbers(10, 4))
        else:
            print("  ✓ PASS: Subtraction works correctly")
    except Exception as e:
        errors.append(f"❌ Subtraction crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test 3: Multiplication
    print("[Test 3/6] Testing multiplication...")
    try:
        if multiply_numbers(6, 7) != 42:
            errors.append("❌ Multiplication failed: multiply_numbers(6, 7) should return 42")
            print("  ✗ FAIL: Expected 42, got", multiply_numbers(6, 7))
        else:
            print("  ✓ PASS: Multiplication works correctly")
    except Exception as e:
        errors.append(f"❌ Multiplication crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test 4: Division
    print("[Test 4/6] Testing division...")
    try:
        result = divide_numbers(20, 4)
        if result != 5.0:
            errors.append("❌ Division failed: divide_numbers(20, 4) should return 5.0")
            print("  ✗ FAIL: Expected 5.0, got", result)
        else:
            print("  ✓ PASS: Division works correctly")
    except Exception as e:
        errors.append(f"❌ Division crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test 5: Division by zero handling
    print("[Test 5/6] Testing division by zero...")
    try:
        result = divide_numbers(10, 0)
        if result is not None:
            errors.append("❌ Division by zero should return None")
            print("  ✗ FAIL: Expected None, got", result)
        else:
            print("  ✓ PASS: Division by zero handled correctly")
    except ZeroDivisionError:
        errors.append("❌ Division by zero caused a crash! Handle it with an if statement")
        print("  ✗ FAIL: Your function crashed instead of returning None")
    except Exception as e:
        errors.append(f"❌ Unexpected error: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test 6: Average
    print("[Test 6/6] Testing average calculation...")
    try:
        if calculate_average(10, 20, 30) != 20.0:
            errors.append("❌ Average failed: calculate_average(10, 20, 30) should return 20.0")
            print("  ✗ FAIL: Expected 20.0, got", calculate_average(10, 20, 30))
        else:
            print("  ✓ PASS: Average calculation works correctly")
    except Exception as e:
        errors.append(f"❌ Average calculation crashed: {e}")
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
        print("\n💡 TIP: Fix the errors above and run the tests again!")
        return False
    else:
        print(" ALL TESTS PASSED! ✅")
        print("=" * 70)
        print("\n🎉 Great job! Your calculator functions work correctly!")
        print("📝 Don't forget to commit your changes:")
        print("   git add exercises/calculator.py")
        print('   git commit -m "Fix calculator functions"')
        return True


if __name__ == "__main__":
    success = test_calculator()
    # Exit with appropriate code for automated testing
    exit(0 if success else 1)
