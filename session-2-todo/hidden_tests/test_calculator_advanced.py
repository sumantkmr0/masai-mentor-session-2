#!/usr/bin/env python3
"""
HIDDEN TEST FILE - Advanced Calculator Tests

These tests check edge cases and additional scenarios.
Students will see these tests when they create a pull request!

This teaches the importance of:
- Edge case testing
- Handling unexpected inputs
- Writing robust code
"""

import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from exercises.calculator import *


def test_calculator_advanced():
    """
    Run advanced calculator tests with edge cases.
    """
    print("\n" + "=" * 70)
    print(" HIDDEN TESTS - Calculator Edge Cases 🔍")
    print("=" * 70)
    print("\nSurprise! These are additional tests to make your code more robust!\n")

    errors = []

    # Test with negative numbers
    print("[Hidden Test 1] Testing with negative numbers...")
    try:
        if add_numbers(-5, 3) != -2:
            errors.append("Addition with negative numbers failed")
            print("  ✗ FAIL: add_numbers(-5, 3) should return -2")
        elif subtract_numbers(-10, -4) != -6:
            errors.append("Subtraction with negative numbers failed")
            print("  ✗ FAIL: subtract_numbers(-10, -4) should return -6")
        elif multiply_numbers(-6, 7) != -42:
            errors.append("Multiplication with negative numbers failed")
            print("  ✗ FAIL: multiply_numbers(-6, 7) should return -42")
        else:
            print("  ✓ PASS: Works with negative numbers!")
    except Exception as e:
        errors.append(f"Negative number test crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test with decimals
    print("[Hidden Test 2] Testing with decimal numbers...")
    try:
        if round(add_numbers(1.5, 2.3), 1) != 3.8:
            errors.append("Addition with decimals failed")
            print("  ✗ FAIL: add_numbers(1.5, 2.3) should return approximately 3.8")
        elif round(multiply_numbers(2.5, 4), 1) != 10.0:
            errors.append("Multiplication with decimals failed")
            print("  ✗ FAIL: multiply_numbers(2.5, 4) should return 10.0")
        else:
            print("  ✓ PASS: Works with decimal numbers!")
    except Exception as e:
        errors.append(f"Decimal number test crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test with zeros
    print("[Hidden Test 3] Testing with zero...")
    try:
        if add_numbers(0, 0) != 0:
            errors.append("Addition with zeros failed")
            print("  ✗ FAIL: add_numbers(0, 0) should return 0")
        elif multiply_numbers(5, 0) != 0:
            errors.append("Multiplication with zero failed")
            print("  ✗ FAIL: multiply_numbers(5, 0) should return 0")
        else:
            print("  ✓ PASS: Handles zero correctly!")
    except Exception as e:
        errors.append(f"Zero test crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test average with different numbers
    print("[Hidden Test 4] Testing average with various inputs...")
    try:
        if calculate_average(5, 5, 5) != 5.0:
            errors.append("Average of same numbers failed")
            print("  ✗ FAIL: calculate_average(5, 5, 5) should return 5.0")
        elif round(calculate_average(1, 2, 3), 2) != 2.0:
            errors.append("Average of sequential numbers failed")
            print("  ✗ FAIL: calculate_average(1, 2, 3) should return 2.0")
        else:
            print("  ✓ PASS: Average calculation is robust!")
    except Exception as e:
        errors.append(f"Average test crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test division edge cases
    print("[Hidden Test 5] Testing division edge cases...")
    try:
        if divide_numbers(0, 5) != 0.0:
            errors.append("Division of zero failed")
            print("  ✗ FAIL: divide_numbers(0, 5) should return 0.0")
        elif round(divide_numbers(1, 3), 2) != 0.33:
            errors.append("Division with repeating decimal failed")
            print("  ✗ FAIL: divide_numbers(1, 3) should return approximately 0.33")
        else:
            print("  ✓ PASS: Division handles edge cases!")
    except Exception as e:
        errors.append(f"Division edge case test crashed: {e}")
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
        print("\n💡 Don't worry! Your basic functionality works.")
        print("   These edge cases help make your code more robust.")
        print("   Consider fixing these for extra practice!")
        return False
    else:
        print(" ALL HIDDEN TESTS PASSED! 🌟")
        print("=" * 70)
        print("\n🎉 Excellent! Your code handles edge cases perfectly!")
        print("   You've written robust, production-ready code!")
        return True


if __name__ == "__main__":
    success = test_calculator_advanced()
    exit(0 if success else 1)
