# Expense Tracker

ExpenseTracker, a Python application,highlights object-oriented programming (OOP) skills in financial expense management. Comprising two pivotal classes, Expense and ExpenseDB, it models individual expenses with attributes like a unique identifier, title, amount, and timestamps in Coordinated Universal Time (UTC). The Expense class features methods for  updating details, and efficient conversion to a dictionary. As a manager for Expense objects, the ExpenseDB class facilitates addition, removal, retrieval of expenses.

## Run Locally

Clone the project

```bash
  git clone https://github.com/lawal-hash/ExpenseTracker.git
```

change working directory


```bash
  cd ExpenseTracker
```

## Usage/Examples

```python
from expense import Expense
from expensedb import ExpenseDatabase


def main():
    expense_one = Expense("Spain", 80.00)
    expense_two = Expense("UK", 180.00)
    expense_three = Expense("Malaga", 300.00)

    expense_db = ExpenseDatabase()

    for expense in [expense_one, expense_two, expense_three]:
        expense_db.add_expense(expense)

if __name__ == "__main__":
    main()

```

```python
python main.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
