from typing import Dict
from expense import Expense


class ExpenseDatabase:
    def __init__(self) -> None:
        pass

    def add_expense(self, expense: Expense) -> None:
        pass

    def remove_expense(self, expense_id: str) -> None:
        pass

    def get_expense_by_id(self, expense_id: str) -> None:
        pass

    def get_expense_by_title(self, expense_title: str) -> None:
        pass

    def to_dict(self) -> Dict:
        pass
