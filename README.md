# IFCS AE2 – Quiz Application

**Python version used:** Python 3.11  
**GUI framework:** Streamlit  
**Storage:** CSV file  
**Repository:** (link submitted separately)

---

## 1. Introduction

This project focuses on the design, implementation, testing, and documentation of a Python‑based quiz application intended for use within an organisational setting. The purpose of the application is to provide an interactive and accessible way to assess knowledge of ethical decision‑making through a multiple‑choice quiz. Ethical judgement is an important skill in many professional environments, and the quiz format offers a simple mechanism for reinforcing understanding while providing immediate feedback to users.

The application was developed using Python 3 and the Streamlit framework. Streamlit was selected because it enables the creation of web‑based interfaces using minimal frontend code, allowing the focus of the project to remain on core programming concepts rather than user interface complexity. Quiz questions are stored externally in a CSV file, which allows content to be updated easily without modifying the application logic. User results are also saved to a CSV file, providing persistent storage so that scores are retained across application runs.

Beyond core functionality, the project aims to demonstrate a professional software development process. Version control is managed using GitHub, enabling incremental development and traceability of changes. Unit tests are written to validate key parts of the application logic, and continuous integration is implemented using GitHub Actions to automatically run tests when code changes are pushed. This approach reflects common industry practices and helps ensure reliability and maintainability.

This report documents the design decisions made throughout the project, explains how the application works by referencing key parts of the codebase, and describes the testing and deployment workflow. By combining practical implementation with clear documentation, the project demonstrates both technical competence and an understanding of fundamental software engineering principles.

---

## 2. Design Section

### GUI Design

The application uses a simple graphical user interface to guide the user through the quiz. The intended user journey is:

1. Open the application  
2. Start the quiz  
3. Answer questions one by one  
4. View the final score  
5. Results stored as a CSV file  

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

**Non‑functional requirements**
- The application is easy to use for non‑technical staff.
- Errors are handled without crashing.
- The code is readable and maintainable.

### Tech Stack

- Python 3.9+
- GUI framework: Streamlit 
- CSV file for persistent storage
- GitHub for version control
- unittest for testing

### Code Design

The application is organised so that different responsibilities are kept separate within the code.
Quiz questions are loaded from a CSV file using a dedicated function, keeping data reading separate from the user interface.
Quiz results are saved to a CSV file using a separate function, allowing results to persist between application runs.
The quiz flow (current question, score, and progress) is managed using Streamlit session state.
Score calculation and result evaluation are handled independently of the user interface logic.
Streamlit is used only for displaying questions, collecting user input, and showing feedback.
This separation makes the code easier to understand, test, and extend in future.

class diagram:

+-------------------+
|   Streamlit UI    |
|-------------------|
| Displays questions|
| Handles buttons   |
| Manages session   |
+---------+---------+
          |
          v
+-------------------+
|   Quiz Logic      |
|-------------------|
| Tracks score      |
| Tracks progress   |
| Calculates result |
+---------+---------+
          |
          v
+-------------------+
| Data Access       |
|-------------------|
| load_questions()  |
| save_result()     |
| CSV files         |
+-------------------+

This design illustrates how the user interface interacts with the quiz logic, while data access functions handle reading and writing CSV files independently of the interface.

---

## 3. Development Section

The development of the application focused on building functionality incrementally. Core features such as loading questions and tracking quiz state were implemented first, followed by result persistence and user feedback. This approach allowed each feature to be tested and validated before adding additional complexity.

Quiz questions are stored externally in a CSV file, allowing the quiz content to be updated without changing the application code. The questions are loaded using the load_questions() function. This function is responsible only for reading data from the CSV file. Using a dedicated function for this task separates data access from the rest of the application logic and improves maintainability. The use of UTF‑8 encoding ensures compatibility with different operating systems and avoids common CSV formatting issues:

<img width="743" height="125" alt="image" src="https://github.com/user-attachments/assets/0631dde5-f0e6-40db-8343-8c427ffa08ce" />

The function appends results to results.csv, creating the file if it does not already exist. This ensures results persist between application runs and can be reviewed later.

<img width="828" height="224" alt="image" src="https://github.com/user-attachments/assets/2ab7e240-ad2d-4a7b-a2af-4ee6c6eb07b8" />

The quiz state (current question and score) is tracked using Streamlit’s session state. The current_q variable stores the index of the current question, while score tracks the number of correct answers. This approach allows the quiz to progress correctly as the user clicks buttons, despite Streamlit’s stateless execution model.

<img width="578" height="130" alt="image" src="https://github.com/user-attachments/assets/622053f6-3e43-409e-a18b-15643c0d730e" />

Each question is displayed dynamically based on the current index stored in session state.

<img width="1021" height="133" alt="image" src="https://github.com/user-attachments/assets/aa938e2d-8b4c-457d-8f44-facc6586ddfe" />

Users select an answer using a radio button, and their response is checked when they click “Next”.

<img width="718" height="109" alt="image" src="https://github.com/user-attachments/assets/206cf8d5-ef12-4dc9-b104-b241ff1d147c" />

Once all questions have been answered, the final score and percentage are calculated and displayed. Conditional logic is used to provide feedback and award badges based on performance, improving user engagement.

<img width="966" height="97" alt="image" src="https://github.com/user-attachments/assets/a6a8bf09-d292-42b6-81bc-bfdc6480f388" />

<img width="722" height="234" alt="image" src="https://github.com/user-attachments/assets/627e701e-00c9-496b-98d3-e5ef881aaa54" />


---

## 4. Testing Section

### Testing Approach

Manual testing was used for the graphical interface because user interaction and visual layout are difficult to validate using automated tests. Automated unit testing was used for logic that does not depend on the Streamlit interface, such as score calculation and result handling. This combination ensures both functional correctness and a usable interface.

### Manual Test Results

| Test Case | Description | Result |
|---------|------------|--------|
| MT1 | Application opens correctly | Pass |
| MT2 | Quiz starts and questions display | Pass |
| MT3 | Score is calculated correctly | Pass |
| MT4 | Results export to CSV | Pass |

### Unit Testing

Unit tests were run using unittest
A screenshot of the tests running successfully is included below.

test run locally:

<img width="486" height="153" alt="image" src="https://github.com/user-attachments/assets/1b8e6ae6-8b20-405f-b3f6-d8b9cc58c9a2" />

github actions- unittest passing:

<img width="388" height="259" alt="image" src="https://github.com/user-attachments/assets/17baefa3-61a5-421e-87bf-8ef5835b4d8b" />

<img width="1342" height="620" alt="image" src="https://github.com/user-attachments/assets/43f38210-2556-4455-86e6-5d652ae98900" />

github actions- unittest failing:

<img width="349" height="190" alt="image" src="https://github.com/user-attachments/assets/e6f4a54a-579e-4a24-8d16-bf5dc98dc7a6" />

<img width="696" height="327" alt="image" src="https://github.com/user-attachments/assets/e8a79dd1-0926-49c2-bdc5-27a4dfe63fca" />


---

## 5. Documentation Section

### User Documentation

The quiz application is designed to be simple to run and use, even for users with limited technical knowledge. The steps below describe how an end user can run the application and interact with it.

To run the application:
1. Ensure that Python version 3.9 or above is installed on the system.
2. Download or clone the project repository from GitHub into VScode.
3. Navigate to the project directory and run the main application file using Streamlit- in the terminal you can run: 'streamlit run app.py'
4. Once the application starts, follow the on‑screen instructions to complete the quiz by answering each question in turn.
5. After completing the quiz, the final score and percentage result are displayed, and the results are automatically saved to a CSV file.

The application interface guides the user through the quiz using clear visual elements such as radio buttons, progress bars, and feedback messages. No manual configuration is required, and all results are saved automatically without user intervention. This design ensures the application is accessible and suitable for use by non‑technical staff in an organisational setting.

### Technical Documentation

-The application is implemented in a single app.py file using Python and the Streamlit framework.

-Quiz questions are stored in a CSV file (questions.csv) and loaded at runtime using a dedicated function, separating data access from application logic.

-Quiz results are written to a CSV file (results.csv) using a separate function, providing persistent storage across application runs.

-Quiz progress and scoring are managed using Streamlit’s session state, allowing the application to track user progress.

-Core quiz logic (such as score updates and question progression) is kept separate from the user interface code to improve readability and maintainability.

-Unit tests are included to validate testable logic such as scoring and input handling.

-Tests can be run locally using the Python test framework from the command line (python -m unittest discover -s tests).

-Continuous integration is configured using GitHub Actions to automatically run unit tests whenever changes are pushed to the repository.

---

## 6. Evaluation Section

The completed quiz application demonstrates a full end‑to‑end development process, from initial design through to implementation, testing, deployment, and documentation. By using Python and the Streamlit framework, the project delivers a functional and user‑friendly application while remaining focused on core programming concepts rather than unnecessary technical complexity. Streamlit proved to be an effective choice for rapidly developing an interactive interface, allowing the project to prioritise application logic, data handling, and testing practices. The use of external CSV files for both question storage and result persistence provides a simple and flexible data solution that meets the project requirements effectively and supports easy content updates without modifying the underlying code.

A key strength of the application is the clear separation of responsibilities within the code. Data loading, result saving, quiz logic, and user interface behaviour are handled in distinct sections of the program. This structure improves readability and maintainability and allows individual parts of the application to be modified or extended without affecting the entire system. For example, new quiz topics could be introduced by changing the question file, or additional result analysis could be added by extending the CSV storage logic. This modular approach reflects good software engineering practice and supports long‑term sustainability of the codebase.

The inclusion of automated unit testing and continuous integration further strengthens the project by ensuring that important logic can be validated consistently. Running tests automatically through GitHub Actions reduces the risk of regression errors and demonstrates an awareness of professional development workflows commonly used in real‑world software projects. Combining automated testing with manual interface testing ensured that both the internal logic and the user experience were thoroughly validated.

Overall, the project successfully meets its objectives by delivering a working quiz application that is well‑structured, testable, and clearly documented. The techniques used in this project—such as separation of concerns, persistent storage, automated testing, and continuous integration—are transferable to a wide range of organisational applications. As a result, this project provides a solid foundation for future development and demonstrates a strong understanding of both practical programming and fundamental software engineering principles.
