# Expense Tracker

A brief description of what this project does and who it's for

## Run Locally

Clone the project

```bash
  git clone https://github.com/lawal-hash/ExpenseTracker.git
```

Install dependencies

```bash
  pip install poetry
  cd ExpenseTracker
  poetry install --no-root
  poetry shell
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
