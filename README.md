# IFCS AE2 – Quiz Application

**Python version used:** Python 3.11  
**GUI framework:** Streamlit  
**Storage:** CSV file  
**Repository:** (link submitted separately)

---

## 1. Introduction

I work in a policy and analytical environment where staff need to understand internal processes, procedures, and good practice. This can be challenging for new starters or when teams change, as information is often spread across documents and informal guidance.

To address this, I developed a simple quiz application intended for use by my employer. The purpose of the quiz is to allow staff to test their knowledge in a quick and consistent way, while also providing feedback and recording results. This supports learning, helps identify gaps in understanding, and encourages good practice.

The application is designed as a minimum viable product (MVP). It focuses on core functionality: presenting questions through a graphical user interface, validating user input, calculating scores, and saving results to a CSV file so they persist between sessions. The system is written in Python using object‑oriented principles and includes documentation, exception handling, and testing to demonstrate a professional development approach.

---

## 2. Design Section

### GUI Design

The application uses a simple graphical user interface to guide the user through the quiz. The intended user journey is:

1. Open the application  
2. Start the quiz  
3. Answer questions one by one  
4. View the final score  
5. Export results to a CSV file  

Screenshots of the GUI and the prototype design are included below.  

<img width="1103" height="791" alt="image" src="https://github.com/user-attachments/assets/925a5457-5150-49e8-b46b-4bbd01cb0ab5" />

<img width="1104" height="704" alt="image" src="https://github.com/user-attachments/assets/7077c2c0-2699-4953-952a-4d6c14f4c89e" />

<img width="1164" height="833" alt="image" src="https://github.com/user-attachments/assets/9d528ffc-65a6-4cad-b602-fb7c5ff305f9" />

results .csv

<img width="428" height="200" alt="image" src="https://github.com/user-attachments/assets/276b2825-4f0c-4c51-8791-04f87af58b5d" />





### Requirements

**Functional requirements**
- The user can start and complete a quiz.
- The application validates user input.
- A score is calculated and displayed at the end.
- Results are saved to a CSV file.
- Results can be exported.

**Non‑functional requirements**
- The application is easy to use for non‑technical staff.
- Errors are handled gracefully without crashing.
- The code is readable and maintainable.

### Tech Stack

- Python 3.9+
- GUI framework: [Tkinter / Streamlit / Flask]
- CSV file for persistent storage
- GitHub for version control
- Pytest (or unittest) for testing

### Code Design

The code is structured using object‑oriented programming. For example:
- A class to manage the quiz logic and scoring
- A class or module to handle CSV storage
- Separate functions for validating user input

This separation makes the code easier to test and extend.

---

## 3. Development Section

The application is written in Python and organised into logical components. The quiz logic controls the flow of questions and scoring, while the GUI handles user interaction.

Persistent storage is implemented using a CSV file. When the quiz is completed, the user’s result is written to the file. If the file does not exist, it is created automatically.

Input validation ensures that users cannot submit invalid or empty answers. Exception handling is used when reading from or writing to the CSV file to prevent crashes and provide clear error messages.

(Insert small, relevant code snippets here if required.)

---

## 4. Testing Section

### Testing Approach

Both manual and automated testing were used.

Manual testing was used to check the graphical interface and user flow, such as starting the quiz, answering questions, and exporting results.

Automated unit tests were used for testable logic such as input validation and scoring. These tests focus on pure functions that return the same output for the same input.

### Manual Test Results

| Test Case | Description | Result |
|---------|------------|--------|
| MT1 | Application opens correctly | Pass |
| MT2 | Quiz starts and questions display | Pass |
| MT3 | Invalid input is rejected | Pass |
| MT4 | Score is calculated correctly | Pass |
| MT5 | Results export to CSV | Pass |

### Unit Testing

Unit tests were run using [pytest/unittest].  
A screenshot of the tests running successfully is included below.

test run locally:
<img width="486" height="153" alt="image" src="https://github.com/user-attachments/assets/1b8e6ae6-8b20-405f-b3f6-d8b9cc58c9a2" />

github actions- unittest passing:

<img width="388" height="259" alt="image" src="https://github.com/user-attachments/assets/17baefa3-61a5-421e-87bf-8ef5835b4d8b" />

<img width="1342" height="620" alt="image" src="https://github.com/user-attachments/assets/43f38210-2556-4455-86e6-5d652ae98900" />

github actions- unittest failing:

<img width="349" height="190" alt="image" src="https://github.com/user-attachments/assets/e6f4a54a-579e-4a24-8d16-bf5dc98dc7a6" />



---

## 5. Documentation Section

### User Documentation

To run the application:
1. Ensure Python 3.9 or above is installed.
2. Download the repository.
3. Run the main application file.
4. Follow the on‑screen instructions to complete the quiz.
5. Use the export option to save results.

### Technical Documentation

- Tests can be run locally using the test framework.
- The CSV file stores quiz results and is updated after each run.
- Input validation functions are written so they can be tested independently.

---

## 6. Evaluation Section

Overall, the project successfully demonstrates the development of a Python application using a professional workflow. The GUI and persistent storage work as intended, and the use of object‑oriented programming helped keep the code organised.

One area that went well was separating logic from the interface, which made testing easier. The main limitation of the current MVP is that it supports only a small number of questions and limited feedback. With more time, the application could be improved by adding more question sets, better visual design, and more detailed reporting.

Despite these limitations, the project meets the requirements of the assignment and provides a solid foundation for a workplace training tool.
