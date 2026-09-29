# Expense Tracker

A simple command-line **Expense Tracker** developed using Python. This project allows users to add, view, modify, delete, and analyze their expenses. It also provides monthly budget management features.

## 1. Project Overview

The Expense Tracker is a menu-driven Python application for managing daily expenses.

The application allows the user to:

* Add new expenses
* View all expenses
* Calculate total expenses
* Find the highest expense
* Delete an expense
* Modify an expense
* Clear all expenses
* Calculate average expenses
* View category-wise expenses
* Count the number of expenses
* View expenses above the average
* View expenses below the average
* Set a monthly budget
* Check budget status

The expenses are stored temporarily in memory using a Python list of dictionaries.

---

## 2. Technologies Used

* **Programming Language:** Python 3
* **Application Type:** Command-Line Application
* **External Libraries:** None
* **Data Storage:** In-memory Python list

---

## 3. Prerequisites

Before running the project, make sure Python 3 is installed on your computer.

### Check Python Installation

Open **Command Prompt / Terminal** and run:

```bash
python --version
```

If that does not work, try:

```bash
python3 --version
```

You should see a Python 3 version, for example:

```text
Python 3.12.0
```

If Python is not installed, install Python 3 from the official Python website.

---

## 4. Project Setup

### Step 1: Download or Clone the Project

Download the project files and extract them into a folder.

If the project is stored in a Git repository, clone it using:

```bash
git clone <repository-url>
```

Then move into the project folder:

```bash
cd expense-tracker
```

---

### Step 2: Create a Virtual Environment

Creating a virtual environment is recommended but not required because this project does not use external packages.

Create the environment:

```bash
python -m venv venv
```

### Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

This project uses only Python's built-in features.

Therefore, **no external dependencies are required**.

You do not need to run `pip install`.

If a `requirements.txt` file is included in the future, dependencies can be installed using:

```bash
pip install -r requirements.txt
```

---

## 6. Configuration

No special configuration is required.

The program can be run directly after installing Python.

### Expense Date Format

When adding an expense, enter the date in the following format:

```text
YYYY-MM-DD
```

Example:

```text
2026-09-30
```

### Expense Amount

Enter the expense amount as a number.

Example:

```text
500
```

or:

```text
500.50
```

---

## 7. Running the Project

Make sure you are inside the project folder.

Run the Python program using:

```bash
python expense_tracker.py
```

If your Python installation uses `python3`, run:

```bash
python3 expense_tracker.py
```

Replace `expense_tracker.py` with the actual Python filename if it is different.

---

## 8. Main Menu

After starting the program, the following menu will appear:

```text
Welcome to the Expense Tracker!

==Menu==:
1. Add Expense
2. View All Expenses
3. View Total Expenses
4. Highest Expense
5. Delete an Expense
6. Modify an Expense
7. Clear all expenses
8. Average of all expenses
9. Category wise expenses
10. Expense count
11. Above average expenses
12. Below average expenses
13. Set Monthly Budget
14. check Budget Status
15. Exit

please Enter your choice (1-15):
```

Enter a number from **1 to 15** to select an operation.

---

## 9. Adding an Expense

Select:

```text
1. Add Expense
```

The program will ask for:

```text
Date
Category
Description
Amount
```

Example:

```text
please enter the date of expense (YYYY-MM-DD): 2026-09-30
please enter the category of expense: Food
please give more details about the expense: Lunch
please enter the amount of expense: ₹ 250
```

The expense will then be added to the expense list.

---

## 10. Viewing Expenses

Select:

```text
2. View All Expenses
```

The program displays all stored expenses along with their:

* Date
* Category
* Description
* Amount

---

## 11. Budget Management

To set a monthly budget, select:

```text
13. Set Monthly Budget
```

Enter the desired budget amount.

Example:

```text
please enter your monthly budget: ₹ 10000
```

To check the budget status, select:

```text
14. check Budget Status
```

The program compares the total expenses with the monthly budget.

---

## 12. Exiting the Program

To exit the Expense Tracker, select:

```text
15. Exit
```

The program will display:

```text
Exiting the Expense Tracker, Goodbye!
```

---

## 13. Important Note About Data Storage

The current version stores expenses **only in memory** using a Python list.

This means that all expenses will be lost when the program is closed.

For permanent storage, the project can later be improved by using:

* CSV files
* JSON files
* SQLite database
* MySQL database

---

## 14. Troubleshooting

### Python command not recognized

If you see an error such as:

```text
'python' is not recognized as an internal or external command
```

make sure Python is installed and added to the system PATH.

### Invalid amount

Enter the amount using numbers only.

Correct:

```text
500
```

Incorrect:

```text
₹500
```

### Invalid choice

The menu accepts choices from:

```text
1 to 15
```

Enter a valid number when prompted.

---

## 15. Project Structure

A simple project structure can be:

```text
Expense-Tracker/
│
├── expense_tracker.py
└── README.md
```

Where:

* `expense_tracker.py` contains the Python source code.
* `README.md` contains project documentation and setup instructions.

---

## 16. Conclusion

The Expense Tracker is a beginner-friendly Python project that demonstrates important programming concepts such as:

* Lists
* Dictionaries
* Loops
* Conditional statements
* Functions such as `sum()` and `max()`
* List comprehensions
* Lambda functions
* User input
* Exception handling
* Menu-driven programming

The project provides a simple way to manage and analyze personal expenses through a command-line interface.

**Happy Coding! 
