# AI Prompt Log and Development Process

**Project:** AI Bug Report Assistant  
**Course:** COSC 4272 Senior Seminar  
**AI Development Tool:** ChatGPT  
**Application AI Model:** Google Gemini

## Overview

During the development of the AI Bug Report Assistant, I used ChatGPT to assist with project planning, Python programming, debugging, deployment, documentation, input validation, automated testing, and continuous integration.

The application itself uses Google's Gemini API to analyze software bugs submitted by users.

This log documents AI-assisted development activities from the original project and its subsequent improvements for the Senior Seminar software development assignment.

Entries summarize actual development conversations. Where available, direct prompts are included. Other entries are descriptions or paraphrases rather than verbatim transcripts.

---

# Part 1 — Original Application Development

## Entry 1: Project Planning

**AI Tool:** ChatGPT

**Task:** Determine how to fulfill the AI assistant requirement for my Senior Seminar portfolio.

**AI Assistance:** ChatGPT recommended developing an AI Bug Report Assistant using Python, Streamlit, and Google's Gemini API.

**Outcome:** I selected the project because it relates to software development, debugging, and programming.

## Entry 2: Building the Interface

**AI Tool:** ChatGPT

**Task:** Develop the initial Streamlit application.

**AI Assistance:** ChatGPT provided Python code for a bug-description text box, programming language dropdown, and Analyze Bug button.

**Outcome:** I created `app.py`, uploaded it to GitHub, and verified that the interface worked.

## Entry 3: Application Deployment

**AI Tool:** ChatGPT

**Task:** Deploy the Python application online.

**AI Assistance:** ChatGPT guided me through creating `requirements.txt` and configuring Streamlit Community Cloud.

**Outcome:** I successfully deployed the application and confirmed that it was accessible in a browser.

## Entry 4: Gemini API Integration

**AI Tool:** ChatGPT

**Task:** Connect the application to an AI model.

**AI Assistance:** ChatGPT explained how to create a Gemini API key, store it using Streamlit Secrets, install the `google-genai` library, and modify `app.py`.

**Outcome:** The application was able to send bug descriptions to the Gemini API.

## Entry 5: Troubleshooting an API Error

**AI Tool:** ChatGPT

**Actual Prompt:** "its been analyzing for almost 2 minutes now. is it supposed to take this long?"

**Problem:** The application was not returning an AI response.

**AI Assistance:** ChatGPT suggested checking Streamlit's application logs and adding exception logging to identify the underlying error.

The logs showed an HTTP 503 error indicating that the selected Gemini model was experiencing high demand.

**Refinement:** I changed the Gemini model to Flash-Lite and tested the application again.

**Outcome:** The application successfully generated a debugging report.

## Entry 6: Documentation and Portfolio Integration

**AI Tool:** ChatGPT

**Task:** Present the completed application professionally.

**AI Assistance:** ChatGPT helped me add the live application URL and GitHub source code link to my portfolio. It also helped structure the project README.

**Outcome:** The project became accessible through my GitHub Pages portfolio.

---

# Part 2 — Dedicated Software Development Repository

## Entry 7: Reviewing the Second Assignment

**AI Tool:** ChatGPT

**Task:** Understand the requirements for the second Senior Seminar AI-assisted software development assignment.

**AI Assistance:** ChatGPT helped review the assignment requirements and determine whether the previously developed AI Bug Report Assistant could be reused.

**Outcome:** I decided to continue developing the existing application instead of creating an unrelated second AI project.

## Entry 8: Creating a Dedicated GitHub Repository

**AI Tool:** ChatGPT

**Task:** Separate the AI Bug Report Assistant from my original portfolio repository.

**AI Assistance:** ChatGPT explained the difference between copying source files into a new repository and preserving the original Git commit history.

**Refinement:** I chose to use GitHub's website rather than command-line Git operations.

**Outcome:** I created a new public repository:

https://github.com/MrAmmarHaf/AI-Bug-Report-Assistant

I uploaded the existing `app.py`, `requirements.txt`, and `ai-prompt-log.md` files. The new repository maintains its own commit history.

## Entry 9: Creating Software Requirements Documentation

**AI Tool:** ChatGPT

**Task:** Document the application's software requirements.

**AI Assistance:** ChatGPT reviewed my actual Python source code and generated functional requirements, non-functional requirements, project objectives, technology stack, scope, and limitations.

**Refinement:** The documentation was written to reflect implemented features rather than claiming the application could automatically repair code.

**Outcome:** I created and committed `requirements.md`.

## Entry 10: Expanding the README

**AI Tool:** ChatGPT

**Task:** Improve the project's README documentation.

**AI Assistance:** ChatGPT helped organize the README into sections covering installation, API configuration, application features, usage instructions, testing, limitations, and future improvements.

**Verification:** I opened the deployed application and confirmed that it successfully generated an AI response to a test bug description.

**Outcome:** I updated and committed `README.md`.

---

# Part 3 — Testing and Error Handling

## Entry 11: Designing Manual Test Cases

**AI Tool:** ChatGPT

**Task:** Verify that the existing application functions correctly.

**AI Assistance:** ChatGPT created a five-case manual testing checklist covering empty input, whitespace-only input, C++ bug analysis, programming language selection, and maximum input length.

**Implementation:** I performed the tests using the deployed Streamlit application.

**Outcome:** All five manual tests passed.

## Entry 12: Documenting Manual Testing

**AI Tool:** ChatGPT

**Task:** Record the results of manual testing.

**AI Assistance:** ChatGPT generated structured testing documentation containing test objectives, execution steps, expected results, actual results, and testing limitations.

**Outcome:** I created and committed `TESTING.md` with five passing manual test cases.

## Entry 13: Improving Gemini API Key Validation

**AI Tool:** ChatGPT

**Task:** Improve error handling when the Gemini API key is missing.

**AI Assistance:** ChatGPT suggested validating the API key before creating the Gemini client.

**Implementation:** I updated `app.py` to check whether `GEMINI_API_KEY` was available and display a specific error message when it was missing.

**Refinement:** My first code modification had incorrect Python indentation. I shared the updated code with ChatGPT, which identified the issue and showed the corrected structure.

**Outcome:** I committed the API key validation improvement.

## Entry 14: Handling Missing Streamlit Secrets

**AI Tool:** ChatGPT

**Task:** Handle situations where the Streamlit secrets configuration does not exist.

**AI Assistance:** ChatGPT suggested wrapping the secrets lookup in a `try/except` block.

**Refinement:** After reviewing my updated code, ChatGPT recommended explicitly handling `StreamlitSecretNotFoundError` alongside `FileNotFoundError` and `KeyError`.

**Outcome:** I committed the updated secrets error-handling code.

## Entry 15: Extracting Reusable Input Validation

**AI Tool:** ChatGPT

**Task:** Improve the application's code organization and testability.

**AI Assistance:** ChatGPT suggested moving the bug-description validation logic into a separate Python function.

**Implementation:** I created `validation.py` containing `is_valid_bug_description()`.

**Refinement:** I then updated `app.py` to import and call the new function instead of directly checking the text input.

**Outcome:** I committed the validation module and its integration into the application.

## Entry 16: Creating Automated Unit Tests

**AI Tool:** ChatGPT

**Task:** Develop automated tests for the validation function.

**AI Assistance:** ChatGPT generated seven test cases using Python's built-in `unittest` framework.

The tests covered empty strings, whitespace-only strings, valid descriptions, surrounding spaces, `None`, numeric values, and strings containing only newlines and tabs.

**Implementation:** I created and committed `test_validation.py`.

**Outcome:** Seven automated tests were added to the project.

---

# Part 4 — Continuous Integration and Verification

## Entry 17: Configuring GitHub Actions

**AI Tool:** ChatGPT

**Task:** Run automated unit tests without manually executing Python commands.

**AI Assistance:** ChatGPT generated a GitHub Actions workflow that checks out the repository, sets up Python 3.11, and executes the test suite.

**Implementation:** I created `.github/workflows/python-tests.yml` using GitHub's web interface.

**Outcome:** GitHub Actions successfully executed the testing workflow after the commit.

## Entry 18: Verifying and Documenting Automated Test Results

**AI Tool:** ChatGPT

**Task:** Verify that the automated tests actually executed and document the results.

**AI Assistance:** ChatGPT guided me through the GitHub Actions interface to inspect the workflow logs.

**Verification:** The logs confirmed that all seven tests executed successfully.

The output included:

```text
Ran 7 tests in 0.000s

OK
```

**Implementation:** I updated `TESTING.md` to include the automated test cases, testing environment, GitHub Actions workflow, and execution results.

**Outcome:** The project now documents five passing manual test cases and seven passing automated unit tests.

---

# Part 5 — Development Reflection

## How AI Assisted Development

ChatGPT helped me:

- Plan and organize the software development process.
- Write and improve Python code.
- Identify and correct indentation errors.
- Implement input validation and API error handling.
- Prepare software requirements and project documentation.
- Design manual and automated tests.
- Configure continuous integration with GitHub Actions.
- Interpret testing results.

## My Responsibilities

Although ChatGPT provided guidance and code suggestions, I was responsible for creating and managing the GitHub repositories, configuring the hosting service, maintaining the API key, applying code changes, running manual tests, examining logs, and verifying results.

I also reviewed and corrected AI-generated code when necessary.

## Lessons Learned

The project demonstrated that AI-assisted development can accelerate software creation, but AI-generated code still requires human review and testing.

One example was the indentation problem encountered while modifying the Gemini API key validation logic. Another was the Gemini API error encountered during initial development, which required examining logs and changing the configured model.

Automated testing also demonstrated the value of separating application logic into reusable functions.

## Current Testing Summary

| Testing Method | Passed | Failed |
|---|---:|---:|
| Manual functional testing | 5 | 0 |
| Automated unit testing | 7 | 0 |
| **Total** | **12** | **0** |

These results describe the tests performed and do not establish that every possible application behavior has been tested.

## Security

The Gemini API key is stored privately using Streamlit Secrets.

The key is not included in the public source code or project documentation.

## Project Links

**GitHub Repository:** https://github.com/MrAmmarHaf/AI-Bug-Report-Assistant

**Live Application:** https://mrammarhaf-ai-bug-assistant.streamlit.app/

**Original Portfolio:** https://mrammarhaf.github.io/github-portfolio/
