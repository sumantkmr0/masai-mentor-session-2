#!/usr/bin/env python3
"""
HIDDEN TEST FILE - Advanced Student Info Tests

These tests check boundary conditions and edge cases.
Students will see these when they create a pull request!

This teaches:
- Boundary testing (testing at the edges of conditions)
- Complex logical conditions
- Real-world edge cases
"""

import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from exercises.student_info import *


def test_student_info_advanced():
    """
    Run advanced student info tests with boundary cases.
    """
    print("\n" + "=" * 70)
    print(" HIDDEN TESTS - Student Info Edge Cases 🔍")
    print("=" * 70)
    print("\nSurprise! These test boundary conditions and edge cases!\n")

    errors = []

    # Test grade boundaries
    print("[Hidden Test 1] Testing grade boundaries...")
    boundary_tests = [
        (90, 'A', "exactly 90"),
        (89, 'B', "just below A"),
        (80, 'B', "exactly 80"),
        (79, 'C', "just below B"),
        (70, 'C', "exactly 70"),
        (69, 'D', "just below C"),
        (60, 'D', "exactly 60"),
        (59, 'F', "just below D")
    ]

    all_passed = True
    for score, expected, description in boundary_tests:
        try:
            result = calculate_grade(score)
            if result != expected:
                errors.append(f"Boundary case {description} (score {score}): expected '{expected}', got '{result}'")
                print(f"  ✗ FAIL: Score {score} ({description}): expected '{expected}', got '{result}'")
                all_passed = False
        except Exception as e:
            errors.append(f"Grade boundary test crashed at {score}: {e}")
            print(f"  ✗ ERROR at score {score}: {e}")
            all_passed = False

    if all_passed:
        print("  ✓ PASS: All grade boundaries correct!")
    print()

    # Test is_passing boundaries
    print("[Hidden Test 2] Testing passing threshold...")
    try:
        if is_passing(60) != True:
            errors.append("is_passing(60) should return True (exactly at threshold)")
            print("  ✗ FAIL: Score 60 should be passing")
        elif is_passing(59) != False:
            errors.append("is_passing(59) should return False (just below threshold)")
            print("  ✗ FAIL: Score 59 should be failing")
        elif is_passing(100) != True:
            errors.append("is_passing(100) should return True")
            print("  ✗ FAIL: Perfect score should be passing")
        elif is_passing(0) != False:
            errors.append("is_passing(0) should return False")
            print("  ✗ FAIL: Zero score should be failing")
        else:
            print("  ✓ PASS: Passing threshold handled correctly!")
    except Exception as e:
        errors.append(f"Passing boundary test crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Test student status edge cases
    print("[Hidden Test 3] Testing student status boundaries...")
    status_edge_cases = [
        (17, 9, "High School", "17 and grade 9"),
        (18, 9, "Keep Studying", "18 but only grade 9"),
        (17, 12, "High School", "17 and grade 12"),
        (18, 11, "Keep Studying", "18 but only grade 11"),
        (20, 12, "College Ready", "20 and grade 12")
    ]

    all_passed = True
    for age, grade, expected, description in status_edge_cases:
        try:
            result = get_student_status(age, grade)
            if result != expected:
                errors.append(f"Status boundary case ({description}): expected '{expected}', got '{result}'")
                print(f"  ✗ FAIL: {description}: expected '{expected}', got '{result}'")
                all_passed = False
        except Exception as e:
            errors.append(f"Student status test crashed at {description}: {e}")
            print(f"  ✗ ERROR: {e}")
            all_passed = False

    if all_passed:
        print("  ✓ PASS: Student status boundaries correct!")
    print()

    # Test attendance boundaries
    print("[Hidden Test 4] Testing attendance percentage boundaries...")
    attendance_boundaries = [
        (90, 100, "Excellent", "exactly 90%"),
        (89, 100, "Good", "just below 90%"),
        (75, 100, "Good", "exactly 75%"),
        (74, 100, "Needs Improvement", "just below 75%"),
        (60, 100, "Needs Improvement", "exactly 60%"),
        (59, 100, "Poor", "just below 60%"),
        (100, 100, "Excellent", "perfect attendance")
    ]

    all_passed = True
    for attended, total, expected, description in attendance_boundaries:
        try:
            result = calculate_attendance_status(attended, total)
            if result != expected:
                errors.append(f"Attendance boundary ({description}): expected '{expected}', got '{result}'")
                print(f"  ✗ FAIL: {description}: expected '{expected}', got '{result}'")
                all_passed = False
        except Exception as e:
            errors.append(f"Attendance test crashed at {description}: {e}")
            print(f"  ✗ ERROR: {e}")
            all_passed = False

    if all_passed:
        print("  ✓ PASS: Attendance boundaries correct!")
    print()

    # Test eligibility boundaries
    print("[Hidden Test 5] Testing eligibility boundaries...")
    eligibility_boundaries = [
        (85, 90, True, "exactly at both thresholds"),
        (84, 90, False, "score just below threshold"),
        (85, 89, False, "attendance just below threshold"),
        (100, 100, True, "perfect scores"),
        (90, 95, True, "above both thresholds")
    ]

    all_passed = True
    for score, attendance, expected, description in eligibility_boundaries:
        try:
            result = check_eligibility(score, attendance)
            if result != expected:
                errors.append(f"Eligibility boundary ({description}): expected {expected}, got {result}")
                print(f"  ✗ FAIL: {description}: expected {expected}, got {result}")
                all_passed = False
        except Exception as e:
            errors.append(f"Eligibility test crashed at {description}: {e}")
            print(f"  ✗ ERROR: {e}")
            all_passed = False

    if all_passed:
        print("  ✓ PASS: Eligibility boundaries correct!")
    print()

    # Test with unusual but valid inputs
    print("[Hidden Test 6] Testing with edge case values...")
    try:
        # Test very high scores
        if calculate_grade(100) != 'A':
            errors.append("calculate_grade(100) should return 'A'")
            print("  ✗ FAIL: Perfect score should be 'A'")
        # Test zero score
        elif calculate_grade(0) != 'F':
            errors.append("calculate_grade(0) should return 'F'")
            print("  ✗ FAIL: Zero score should be 'F'")
        # Test full attendance
        elif calculate_attendance_status(20, 20) != "Excellent":
            errors.append("Full attendance should be 'Excellent'")
            print("  ✗ FAIL: Perfect attendance should be 'Excellent'")
        else:
            print("  ✓ PASS: Edge case values handled correctly!")
    except Exception as e:
        errors.append(f"Edge case value test crashed: {e}")
        print(f"  ✗ ERROR: {e}")
    print()

    # Print summary
    print("=" * 70)
    if errors:
        print(" SOME HIDDEN TESTS FAILED ⚠️")
        print("=" * 70)
        print(f"\nFound {len(errors)} boundary/edge case issues:")
        for i, error in enumerate(errors, 1):
            print(f"  {i}. {error}")
        print("\n💡 LEARNING MOMENT:")
        print("   Boundary testing is crucial in real-world applications!")
        print("   These test cases help ensure your logic is exactly right.")
        print("   Pay special attention to >= vs > and <= vs < operators.")
        return False
    else:
        print(" ALL HIDDEN TESTS PASSED! 🌟")
        print("=" * 70)
        print("\n🎉 Outstanding! Your logic handles all edge cases!")
        print("   You understand boundary conditions perfectly!")
        print("   This is professional-level code quality!")
        return True


if __name__ == "__main__":
    success = test_student_info_advanced()
    exit(0 if success else 1)
