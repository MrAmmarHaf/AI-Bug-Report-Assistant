# AI Bug Report Assistant — Testing Documentation

## 1. Testing Overview

This document records manual testing performed on the AI Bug Report Assistant, a Python and Streamlit application that uses Google Gemini to generate debugging suggestions.

The purpose of testing was to verify that the application's primary features work correctly, including input validation, programming language selection, AI analysis, and character limits.

**Testing Date:** November 18, 2026

**Testing Environment:** Deployed Streamlit web application

**Application URL:** https://mrammarhaf-ai-bug-assistant.streamlit.app/

**Testing Method:** Manual functional testing

## 2. Test Cases and Results

### Test 1 — Empty Bug Description

**Objective:** Verify that the application rejects empty bug descriptions.

**Steps:**
1. Leave the bug description field empty.
2. Click "Analyze Bug."

**Expected Result:** The application displays a warning asking the user to describe the bug.

**Actual Result:** Test passed. The application displayed the expected validation behavior.

**Status:** PASS

### Test 2 — Whitespace-Only Input

**Objective:** Verify that whitespace-only descriptions are rejected.

**Steps:**
1. Enter only spaces into the bug description field.
2. Click "Analyze Bug."

**Expected Result:** The application rejects the input and displays a warning.

**Actual Result:** Test passed. The application rejected whitespace-only input.

**Status:** PASS

### Test 3 — Valid C++ Bug Analysis

**Objective:** Verify that the application can generate debugging suggestions for a valid C++ problem.

**Steps:**
1. Select C++ as the programming language.
2. Enter: "My program crashes when I access an array outside its bounds."
3. Click "Analyze Bug."

**Expected Result:** The application displays AI-generated debugging guidance.

**Actual Result:** Test passed. The application generated an AI analysis.

**Status:** PASS

### Test 4 — Programming Language Selection

**Objective:** Verify that the application can analyze bugs in another supported programming language.

**Steps:**
1. Select Python as the programming language.
2. Enter: "My program raises a KeyError when reading a dictionary."
3. Click "Analyze Bug."

**Expected Result:** The application provides debugging suggestions relevant to Python.

**Actual Result:** Test passed. The application returned debugging guidance for the selected language.

**Status:** PASS

### Test 5 — Maximum Input Length

**Objective:** Verify that the bug description field enforces the maximum character limit.

**Steps:**
1. Attempt to enter a bug description longer than 3,000 characters.
2. Observe the text input behavior.

**Expected Result:** The application limits the bug description to 3,000 characters.

**Actual Result:** Test passed. The input field enforced the configured character limit.

**Status:** PASS

## 3. Test Summary

| Test ID | Test Description | Result |
|---|---|---|
| TC-01 | Empty bug description | PASS |
| TC-02 | Whitespace-only input | PASS |
| TC-03 | Valid C++ bug analysis | PASS |
| TC-04 | Programming language selection | PASS |
| TC-05 | Maximum input length | PASS |

**Total Tests:** 5

**Passed:** 5

**Failed:** 0

**Pass Rate:** 100%

## 4. Testing Limitations

The tests were performed manually through the deployed web application.

The following areas were not included in this test session:

- Automated unit testing.
- Simulated Gemini API outages.
- Invalid or missing API key scenarios.
- Network connectivity failures.
- Performance and load testing.
- Security penetration testing.

These areas may be evaluated in future testing.

## 5. Conclusion

All five manual functional tests passed.

The results demonstrate that the application's core user-facing features, including input validation, language selection, AI-generated analysis, and character limits, behaved as expected during this test session.

## 6. Automated Unit Testing

Automated unit tests were implemented using Python's built-in `unittest` framework.

The tests verify the reusable `is_valid_bug_description()` function in `validation.py`.

### Automated Test Cases

| Test | Description | Result |
|---|---|---|
| test_empty_description | Rejects empty strings | PASS |
| test_whitespace_only | Rejects whitespace-only strings | PASS |
| test_valid_description | Accepts valid bug descriptions | PASS |
| test_description_with_surrounding_spaces | Accepts descriptions with surrounding spaces | PASS |
| test_none_input | Rejects None values | PASS |
| test_numeric_input | Rejects numeric input | PASS |
| test_newlines_and_tabs | Rejects strings containing only newlines and tabs | PASS |

### Testing Environment

- Framework: Python unittest
- Python Version: 3.11
- Automation Platform: GitHub Actions
- Operating System: Ubuntu (GitHub-hosted runner)
- Execution Date: November 18, 2026
- Workflow: `.github/workflows/python-tests.yml`

### Execution Results

The GitHub Actions workflow successfully discovered and executed all seven tests.

```text
Ran 7 tests in 0.000s

OK
```

**Total Automated Tests:** 7

**Passed:** 7

**Failed:** 0

**Pass Rate:** 100%

### Continuous Integration

GitHub Actions was configured to execute automated tests when changes are pushed to the repository, when pull requests are opened or updated, and when the workflow is manually triggered.

The workflow completed successfully during both its initial automatic execution and a subsequent manual execution.

### Testing Limitations

The automated tests currently cover the input-validation function only. They do not test Gemini API communication, Streamlit interface behavior, or API error handling.

### Conclusion

The seven automated unit tests passed successfully, confirming that the input-validation function behaves as expected for the tested inputs.

Combined with the five previously completed manual functional tests, the project now has 12 passing test cases across two testing approaches.
