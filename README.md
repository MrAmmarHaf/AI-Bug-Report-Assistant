# AI Bug Report Assistant

An AI-powered software debugging assistant developed using Python, Streamlit, and Google's Gemini API.

## 1. Project Overview

The AI Bug Report Assistant is a web-based application designed to help programmers understand and troubleshoot software bugs. Users describe a programming problem, select a programming language, and receive AI-generated explanations, possible causes, debugging steps, and suggested fixes.

The application provides troubleshooting guidance rather than automatically executing or repairing source code.

**Live Application:** https://mrammarhaf-ai-bug-assistant.streamlit.app/

**GitHub Repository:** https://github.com/MrAmmarHaf/AI-Bug-Report-Assistant

## 2. Features

- **Bug Description Input:** Users can enter a bug description containing up to 3,000 characters.
- **Multiple Programming Languages:** Supports C++, Python, Java, JavaScript, and Other.
- **AI-Powered Analysis:** Uses Google Gemini to generate troubleshooting recommendations.
- **Structured Responses:** Organizes results into five sections:
  1. Problem Summary
  2. Possible Causes
  3. Debugging Steps
  4. Suggested Fixes
  5. Additional Information Needed
- **Input Validation:** Prevents empty bug descriptions from being submitted.
- **Error Handling:** Displays a user-friendly message when an API request fails and logs technical error information.
- **Browser-Based Interface:** Accessible through Streamlit.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application programming language |
| Streamlit | Web application framework |
| Google Gemini API | AI-powered debugging analysis |
| Google Gen AI Python SDK | Communication with Gemini |
| GitHub | Version control and source code hosting |
| Streamlit Community Cloud | Web application deployment |

## 4. Installation Instructions

To run the application locally:

**Step 1: Clone the repository**

```bash
git clone https://github.com/MrAmmarHaf/AI-Bug-Report-Assistant.git
```

**Step 2: Navigate to the project directory**

```bash
cd AI-Bug-Report-Assistant
```

**Step 3: Install dependencies**

Ensure Python and pip are installed, then run:

```bash
python -m pip install -r requirements.txt
```

**Step 4: Configure the Gemini API key**

Create a folder named `.streamlit` inside the project directory.

Inside that folder, create a file named `secrets.toml` with the following contents:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Replace the placeholder with your own Google Gemini API key.

**Important:** Never commit `secrets.toml` or your actual API key to a public GitHub repository. Add `.streamlit/secrets.toml` to your local `.gitignore` file.

**Step 5: Run the application**

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL where the application can be accessed in a web browser.

## 5. How to Use the Application

1. Open the live application or run it locally.
2. Enter a description of the software bug.
3. Select the programming language.
4. Click **Analyze Bug**.
5. Wait for Gemini to generate the analysis.
6. Review the possible causes, debugging steps, and suggested fixes.
7. Apply and verify any suggested changes in your own development environment.

## 6. Example Use Case

**Programming Language:** C++

**Example Bug Description:**

"My C++ program crashes when I try to access an array using an index that is larger than the array size. How can I identify and fix the problem?"

The application can provide guidance about out-of-bounds array access, possible indexing errors, debugging techniques, and methods for preventing similar issues.

The exact response may vary because the analysis is AI-generated.

## Application Screenshots

### Bug Submission and AI Analysis

The user enters a C++ bug description, selects the programming language, and receives AI-generated debugging guidance.

![Bug submission and AI analysis](Screenshot1.png)

### Possible Causes and Debugging Steps

The application identifies possible causes and recommends debugging techniques, including debuggers and AddressSanitizer.

![AI debugging recommendations](Screenshot2.png)

## 7. Testing and Validation

The application has been manually tested using programming bug descriptions.

The following behaviors have been reviewed:

- Successful loading of the Streamlit application.
- Submission of a bug description.
- Selection of a programming language.
- Generation and display of an AI response.
- Readable presentation of troubleshooting guidance.

The application also implements validation for empty descriptions and handling for unsuccessful API requests. These safeguards are present in the code but are not claimed here as separately verified test results.

Automated unit testing has not yet been implemented.

## 8. Limitations

- The application cannot automatically compile or execute code.
- It does not directly modify source files.
- It cannot guarantee that the suggested solution is correct.
- The quality of the analysis depends on the information provided by the user.
- An internet connection and access to the Gemini API are required.
- AI service availability and response times may vary.
- The application does not currently store a history of submitted bug reports.

## 9. Project Documentation

Additional documentation is available in this repository:

- [Software Requirements](requirements.md)
- [AI Development Prompt Log](ai-prompt-log.md)

The software requirements document describes the functional requirements, non-functional requirements, scope, assumptions, and development phases.

The AI prompt log documents how AI tools were used during development.

## 10. Future Improvements

Potential improvements include:

- Allowing users to submit source code alongside bug descriptions.
- Adding support for more programming languages.
- Implementing automated unit tests.
- Providing downloadable debugging reports.
- Improving API error handling and user feedback.

## 11. Developer

Developed by Ammar Hafez as part of the COSC 4272 Senior Seminar coursework at Lamar University.

Bachelor of Science in Computer Game Development — Expected Graduation: Summer 2027.
