#!/usr/bin/env python3
"""
Test file for student_info.py

This file tests your student information functions.
Run this to check if your logic is correct!

Usage:
    python tests/test_student_info.py

WHAT YOU'RE LEARNING:
- How to test conditional logic
- Why proper if-elif-else structure matters
- How to test multiple cases thoroughly
"""

import sys
import os

# Add the parent directory to the path so we can import from exercises
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from exercises.student_info import *


def test_student_info():
    """
    Run all student info tests.

    Tests each function with multiple test cases to ensure correct logic.
    """
    print("\n" + "=" * 70)
    print(" STUDENT INFO TESTS - Basic Test Suite")
    print("=" * 70 + "\n")

    errors = []
    test_count = 0

    # Test 1: calculate_grade
    print("[Test 1/5] Testing grade calculation...")
    grade_tests = [
        (95, 'A', "Score 95"),
        (85, 'B', "Score 85"),
        (75, 'C', "Score 75"),
        (65, 'D', "Score 65"),
        (55, 'F', "Score 55")
    ]

    all_grades_pass = True
    for score, expected, description in grade_tests:
        test_count += 1
        try:
            result = calculate_grade(score)
            if result != expected:
                errors.append(f"calculate_grade({score}) should return '{expected}', got '{result}'")
                print(f"  ✗ {description}: Expected '{expected}', got '{result}'")
                all_grades_pass = False
            else:
                print(f"  ✓ {description}: Correct ('{expected}')")
        except Exception as e:
            errors.append(f"calculate_grade crashed with score {score}: {e}")
            print(f"  ✗ ERROR: {e}")
            all_grades_pass = False

    if all_grades_pass:
        print("  ✅ Grade calculation works correctly!")
    print()

    # Test 2: is_passing
    print("[Test 2/5] Testing passing check...")
    passing_tests = [
        (70, True, "Score 70 (passing)"),
        (60, True, "Score 60 (passing)"),
        (59, False, "Score 59 (failing)"),
        (50, False, "Score 50 (failing)")
    ]

    all_passing_pass = True
    for score, expected, description in passing_tests:
        test_count += 1
        try:
            result = is_passing(score)
            if result != expected:
                errors.append(f"is_passing({score}) should return {expected}, got {result}")
                print(f"  ✗ {description}: Expected {expected}, got {result}")
                all_passing_pass = False
            else:
                print(f"  ✓ {description}: Correct ({expected})")
        except Exception as e:
            errors.append(f"is_passing crashed with score {score}: {e}")
            print(f"  ✗ ERROR: {e}")
            all_passing_pass = False

    if all_passing_pass:
        print("  ✅ Passing check works correctly!")
    print()

    # Test 3: get_student_status
    print("[Test 3/5] Testing student status...")
    status_tests = [
        (16, 10, "High School", "Age 16, Grade 10"),
        (17, 9, "High School", "Age 17, Grade 9"),
        (18, 12, "College Ready", "Age 18, Grade 12"),
        (19, 12, "College Ready", "Age 19, Grade 12"),
        (15, 8, "Keep Studying", "Age 15, Grade 8"),
        (16, 8, "Keep Studying", "Age 16, Grade 8")
    ]

    all_status_pass = True
    for age, grade, expected, description in status_tests:
        test_count += 1
        try:
            result = get_student_status(age, grade)
            if result != expected:
                errors.append(f"get_student_status({age}, {grade}) should return '{expected}', got '{result}'")
                print(f"  ✗ {description}: Expected '{expected}', got '{result}'")
                all_status_pass = False
            else:
                print(f"  ✓ {description}: Correct ('{expected}')")
        except Exception as e:
            errors.append(f"get_student_status crashed: {e}")
            print(f"  ✗ ERROR: {e}")
            all_status_pass = False

    if all_status_pass:
        print("  ✅ Student status works correctly!")
    print()

    # Test 4: calculate_attendance_status
    print("[Test 4/5] Testing attendance status...")
    attendance_tests = [
        (18, 20, "Excellent", "90% attendance"),
        (19, 20, "Excellent", "95% attendance"),
        (16, 20, "Good", "80% attendance"),
        (15, 20, "Good", "75% attendance"),
        (13, 20, "Needs Improvement", "65% attendance"),
        (10, 20, "Poor", "50% attendance")
    ]

    all_attendance_pass = True
    for attended, total, expected, description in attendance_tests:
        test_count += 1
        try:
            result = calculate_attendance_status(attended, total)
            if result != expected:
                errors.append(f"calculate_attendance_status({attended}, {total}) should return '{expected}', got '{result}'")
                print(f"  ✗ {description}: Expected '{expected}', got '{result}'")
                all_attendance_pass = False
            else:
                print(f"  ✓ {description}: Correct ('{expected}')")
        except Exception as e:
            errors.append(f"calculate_attendance_status crashed: {e}")
            print(f"  ✗ ERROR: {e}")
            all_attendance_pass = False

    if all_attendance_pass:
        print("  ✅ Attendance status works correctly!")
    print()

    # Test 5: check_eligibility
    print("[Test 5/5] Testing honors eligibility...")
    eligibility_tests = [
        (90, 95, True, "Score 90, Attendance 95%"),
        (85, 90, True, "Score 85, Attendance 90%"),
        (90, 85, False, "Score 90, Attendance 85%"),
        (80, 95, False, "Score 80, Attendance 95%"),
        (84, 90, False, "Score 84, Attendance 90%")
    ]

    all_eligibility_pass = True
    for score, attendance, expected, description in eligibility_tests:
        test_count += 1
        try:
            result = check_eligibility(score, attendance)
            if result != expected:
                errors.append(f"check_eligibility({score}, {attendance}) should return {expected}, got {result}")
                print(f"  ✗ {description}: Expected {expected}, got {result}")
                all_eligibility_pass = False
            else:
                print(f"  ✓ {description}: Correct ({expected})")
        except Exception as e:
            errors.append(f"check_eligibility crashed: {e}")
            print(f"  ✗ ERROR: {e}")
            all_eligibility_pass = False

    if all_eligibility_pass:
        print("  ✅ Eligibility check works correctly!")
    print()

    # Print summary
    print("=" * 70)
    if errors:
        print(" TESTS FAILED ❌")
        print("=" * 70)
        print(f"\nRan {test_count} tests, found {len(errors)} errors:\n")
        for i, error in enumerate(errors, 1):
            print(f"  {i}. {error}")
        print("\n💡 TIPS:")
        print("  - Double-check your if-elif-else conditions")
        print("  - Make sure you're using the right comparison operators (>=, <=, <, >)")
        print("  - Check that return values match exactly (case-sensitive!)")
        print("  - Test your functions manually before running the tests")
        return False
    else:
        print(" ALL TESTS PASSED! ✅")
        print("=" * 70)
        print(f"\n🎉 Perfect! All {test_count} tests passed!")
        print("📝 Don't forget to commit your changes:")
        print("   git add exercises/student_info.py")
        print('   git commit -m "Fix student info logic errors"')
        return True


if __name__ == "__main__":
    success = test_student_info()
    # Exit with appropriate code for automated testing
    exit(0 if success else 1)
