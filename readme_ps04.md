# PS No. 4: Quiz Application

- **Course:** Bachelor of Computer Application (BCA) — 1st Semester (Section 1A)
- **Subject:** Programming Fundamentals Using Python (`RU-100-05-00058`)
- **Institution:** Rungta International Skills University

---

## 📌 About The Project

This is a 1st semester BCA Python project (**PS No. 4: Quiz Application**). It is a console-based multiple-choice quiz application that stores a bank of 10 questions using a list of dictionaries, selects questions using Python's `random` module (or fixed test order when `TEST_MODE = True`), validates user input (`A`, `B`, `C`, or `D`), tracks the score, and displays the final score, percentage, and `Pass`/`Fail` result based on a 50% passing threshold.

---

## ✨ Features

- **Question Bank (List of Dictionaries):** Stores 10 Python multiple-choice questions, where each item contains the `"question"`, `"options"` dictionary (`A`, `B`, `C`, `D`), and `"answer"`.
- **Random & Test Mode Selection:** Uses `random.sample()` to pick questions randomly during normal play, or `TEST_MODE = True` to run the first 3 official test questions in fixed order.
- **Input Validation Loop:** Uses a `while True` loop to check that the user enters only `A`, `B`, `C`, or `D`. Invalid inputs show an error message without losing the question attempt.
- **Score, Percentage & Pass/Fail Calculation:** Calculates `(score / total) * 100`, formats percentage to 2 decimal places, and checks if the score is at least `50%`.

---

## 📁 Files in this Repository

1. **`quiz_application.py`** (or `projject code.py`) — Complete Python 3 source code.
2. **`Project_Report_PS04.pdf`** — Complete project report with logic flow, score chart, test case outputs, and viva questions.
3. **`README.md`** — Project documentation and usage guide.

---

## ⚙️ How to Run

1. Open terminal or Command Prompt in the project directory.
2. Run the Python file directly (no external libraries required):
   ```bash
   python quiz_application.py
   ```

---

## 🧪 Evaluation Test Cases (PS No. 4)

### Test Case 1: Normal Input
- **Input:** `Answers: B, B, C`
- **Output:**
  ```text
  Score: 3/3 | Percentage: 100.00%
  Result: Pass
  ```

### Test Case 2: Boundary / Minimum Input
- **Input:** `Answers: A, A, A`
- **Output:**
  ```text
  Score: 0/3 | Percentage: 0.00%
  Result: Fail
  Correct answers: B, B, C
  ```

### Test Case 3: Invalid Input
- **Input:** `Q1 answer: E, then B`
- **Output:**
  ```text
  Invalid option. Enter A, B, C or D.
  (Q1 is asked again) Correct!
  ```

### Test Case 4: Different Valid Scenario
- **Input:** `Answers: B, A, C`
- **Output:**
  ```text
  Q2 Wrong. Correct answer: B
  Score: 2/3 | Percentage: 66.67% | Result: Pass
  ```
