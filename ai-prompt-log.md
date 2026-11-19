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

---

# Part 6 — Detailed AI Prompt and Response Records

This section provides ten detailed examples of actual ChatGPT interactions during the AI Bug Report Assistant's development and documentation.

The prompts are reproduced from the development conversation. AI response excerpts are shortened where appropriate and are labeled accordingly. Student refinements and implementation outcomes are documented separately.

## Interaction 1 — Reviewing the Application Source Code

**AI Tool:** ChatGPT

**Prompt Submitted:** I submitted the complete Python source code for my AI Bug Report Assistant, including its Streamlit interface, programming language selection, Gemini API integration, and error handling.

**AI-Generated Response (excerpt):**

"Your application currently supports:

- Five programming language selections: C++, Python, Java, JavaScript, and Other.
- Bug descriptions up to 3,000 characters.
- Input validation to prevent empty submissions.
- Google Gemini integration for AI-powered debugging suggestions."

**Student Modifications or Refinements:** I used the code review to ensure the software documentation reflected the application's actual functionality rather than features that had not been implemented.

**Final Implementation Result:** Created `requirements.md` documenting the application's functional requirements, non-functional requirements, assumptions, scope, and limitations.

## Interaction 2 — Verifying the Deployed Application

**AI Tool:** ChatGPT

**Actual Prompt:**

"yeah I just tried it. At first it asked me to wake up the application. I clicked the button and it was 'in the oven' for a minute and then it took me to the official main page of it. I tried testing with my program keeps crashing and it replied so yes its working."

**AI-Generated Response (excerpt):**

"That confirms your AI Bug Report Assistant is deployed and functioning correctly."

ChatGPT explained that Streamlit applications may enter a sleep state after inactivity and guided the creation of a more complete README.

**Student Modifications or Refinements:** I verified that the deployed application could accept a bug description and return an AI-generated response.

**Final Implementation Result:** Updated `README.md` with installation instructions, usage guidance, features, technology information, and limitations.

## Interaction 3 — Reporting Manual Testing Results

**AI Tool:** ChatGPT

**Actual Prompt:**

"I completed the five AI Bug Report Assistant manual tests. Results: Empty description: pass; Whitespace-only description: pass; Valid C++ bug: pass; Language selection: pass; Input length: pass. Let's document the results and continue."

**AI-Generated Response (excerpt):**

"All five manual tests passed. That gives us documented evidence that the application's core functionality is working."

ChatGPT prepared testing documentation containing objectives, steps, expected results, actual results, and testing limitations.

**Student Modifications or Refinements:** I manually executed the five test cases in the deployed application and reported the observed results.

**Final Implementation Result:** Created `TESTING.md` with five passing manual functional tests.

## Interaction 4 — Correcting Python Indentation

**AI Tool:** ChatGPT

**Prompt Submitted:** I pasted an updated version of `app.py` and asked, "like this", after adding API key validation code.

**AI-Generated Response (excerpt):**

"Almost! You're very close. The only issue is Python indentation."

ChatGPT explained that the new API key validation statements needed to remain inside the `with st.spinner(...)` block.

**Student Modifications or Refinements:** I corrected the indentation and resubmitted the Python source code for review.

**Final Implementation Result:** Updated `app.py` with properly indented API key validation and committed the change.

## Interaction 5 — Reviewing Missing Secrets Error Handling

**AI Tool:** ChatGPT

**Actual Prompt (excerpt):**

```python
try:
    api_key = st.secrets.get("GEMINI_API_KEY")
except (FileNotFoundError, KeyError):
    api_key = None
```

"like this?"

**AI-Generated Response (excerpt):**

"Your indentation is correct, and you've placed the new try/except block in the right location."

ChatGPT recommended adding `st.errors.StreamlitSecretNotFoundError` to the exception handling.

**Student Modifications or Refinements:** I changed the exception handler to:

```python
except (FileNotFoundError, KeyError, st.errors.StreamlitSecretNotFoundError):
    api_key = None
```

**Final Implementation Result:** Committed improved handling for missing Streamlit secrets configurations.

## Interaction 6 — Creating a Reusable Validation Function

**AI Tool:** ChatGPT

**Actual Prompt:** "ok committed"

This was a continuation after committing the previous error-handling improvement.

**AI-Generated Response (excerpt):**

"We'll start with a small improvement: moving your input-validation logic into a reusable function."

ChatGPT provided the following implementation:

```python
def is_valid_bug_description(description):
    """Return True if the description contains non-whitespace text."""
    return isinstance(description, str) and bool(description.strip())
```

**Student Modifications or Refinements:** I created `validation.py` and subsequently modified `app.py` to import and use `is_valid_bug_description()`.

**Final Implementation Result:** The application's input-validation logic was separated into a reusable, independently testable Python module.

## Interaction 7 — Developing Automated Unit Tests

**AI Tool:** ChatGPT

**Actual Prompt:** "ok committed lets continue"

This prompt followed the integration of the validation function into `app.py`.

**AI-Generated Response (excerpt):**

"We're now ready to add automated unit tests, which will give your professor evidence that you've gone beyond simply building an application."

ChatGPT provided seven tests using Python's `unittest` framework, including:

```python
def test_empty_description(self):
    self.assertFalse(is_valid_bug_description(""))

def test_valid_description(self):
    self.assertTrue(
        is_valid_bug_description("My C++ program crashes.")
    )
```

**Student Modifications or Refinements:** I created `test_validation.py` and added the seven test cases.

**Final Implementation Result:** Added automated tests covering valid descriptions, empty input, whitespace, surrounding spaces, non-string input, and newline/tab characters.

## Interaction 8 — Configuring GitHub Actions

**AI Tool:** ChatGPT

**Actual Prompt:** "ok committed"

This prompt followed the creation of `test_validation.py`.

**AI-Generated Response (excerpt):**

"GitHub Actions lets GitHub automatically execute your Python tests whenever you push changes to your repository."

ChatGPT generated a workflow using `actions/checkout@v4`, `actions/setup-python@v5`, and the command:

```bash
python -m unittest discover -v
```

**Student Modifications or Refinements:** I created `.github/workflows/python-tests.yml` using GitHub's web interface and manually triggered an additional workflow run.

**Final Implementation Result:** Configured continuous integration to execute the validation tests automatically on pushes and pull requests, with an option for manual execution.

## Interaction 9 — Verifying Automated Test Execution

**AI Tool:** ChatGPT

**Prompt Submitted:** I uploaded screenshots of the GitHub Actions workflow and its execution logs.

**AI-Generated Response (excerpt):**

"Your screenshot confirms that all seven automated unit tests passed successfully!"

ChatGPT identified the test output:

```text
Ran 7 tests in 0.000s

OK
```

**Student Modifications or Refinements:** I opened the GitHub Actions job logs and verified that each of the seven tests reported `ok`.

**Final Implementation Result:** Updated `TESTING.md` to document the seven passing automated tests and the successful GitHub Actions workflow.

## Interaction 10 — Troubleshooting README Screenshot Paths

**AI Tool:** ChatGPT

**Prompt Submitted:** I uploaded screenshots showing that the images in my GitHub README were not displaying correctly. One screenshot showed a GitHub 404 error.

**AI-Generated Response (excerpt):**

"I see the problem! Your screenshots uploaded successfully, but the filenames in your README don't match the actual filenames on GitHub."

ChatGPT identified the mismatch between the README references and the uploaded image filenames.

**Student Modifications or Refinements:** I changed the Markdown image paths from `Screenshot1(1).png` and `Screenshot2(1).png` to the actual repository filenames.

**Final Implementation Result:** Both application demonstration screenshots displayed correctly in `README.md`.

---

## Detailed Interaction Summary

These ten records demonstrate how ChatGPT was used for software requirements analysis, documentation, debugging, input validation, code modularization, automated testing, continuous integration, and troubleshooting.

The development process involved reviewing AI-generated suggestions, modifying source code, testing the application, examining results, and committing verified improvements to GitHub.

The original development activities and additional AI-assisted work are documented in Parts 1–5 of this log.
