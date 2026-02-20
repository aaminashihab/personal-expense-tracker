#  Personal Expense Tracker

A modular, CLI-based Expense Tracking application built using **Python** and **Object-Oriented Programming (OOP)** principles.
Designed with clean project structure and separation of concerns to simulate real-world backend architecture.

---

##  Features

*  Add expenses with date validation
*  View total expenses
*  Category-wise expense analysis
*  Identify highest spending category
*  Percentage distribution using NumPy
*  Monthly expense summary
*  Input validation with exception handling
*  Clean modular architecture

---

##  Project Structure

```
personal_expense_tracker/
│
├── models/
│   └── expense.py          # Expense data model
│
├── services/
│   └── tracker.py          # Business logic layer
│
├── utils/
│   └── validators.py       # Input validation utilities
│
├── main.py                 # CLI interface
├── pyproject.toml          # Project configuration
└── README.md               # Documentation
```

---

##  Architecture Overview

###  Models Layer

Defines the `Expense` class:

* Stores amount
* Stores category
* Converts and validates date (`YYYY-MM-DD` format)

###  Services Layer

Contains `ExpenseTracker` class:

* Manages expense storage
* Performs total calculation
* Generates category analysis
* Computes percentage distribution
* Filters monthly summaries

###  Utils Layer

Provides reusable validation functions:

* `get_float_input()`
* `get_int_input()`

###  Main Layer

Handles:

* CLI menu interaction
* User input
* Exception handling
* Output formatting

---

##  How to Run

### 1️ Clone Repository

```bash
git clone https://github.com/aaminashihab/personal_expense_tracker
cd personal_expense_tracker
```

### 2️ Install Dependencies

```bash
uv add numpy
```

### 3️ Run Application

```bash
python main.py
```

---

##  Sample CLI Menu

```
=== Personal Expense Tracker ===
1. Add Expense
2. View Total Expense
3. View Category-wise Total
4. View Highest Spending Category
5. View Percentage Analysis
6. Monthly Summary
7. Exit
```

---

##  Example Outputs

**Category-wise Total**

```
Food: ₹2500
Travel: ₹1800
```

**Highest Spending**

```
Highest Spending: Food (₹2500)
```

**Percentage Analysis**

```
Food: 58.14%
Travel: 41.86%
```

---

##  Technologies Used

* Python 3.14
* NumPy
* OOP Principles
* Modular Project Design

---

##  Learning Outcomes

* Clean architecture separation (Models / Services / Utils)
* Business logic abstraction
* Data validation practices
* CLI application design
* Foundational analytical computation using NumPy

---

##  Future Enhancements

* CSV/JSON file persistence
* database integration
* Data visualization 
* Pandas-based analytics
* Web version 
* Unit testing integration

---





