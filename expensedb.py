import logging
from typing import Dict, List
from expense import Expense


class ExpenseDatabase:
    """
    Manages a collection of Expense objects
    """

    def __init__(self) -> None:
        self.expenses = []

    def __repr__(self) -> str:
        return "ExpenseDatabase()"

    def __len__(self) -> int:
        return len(self.expenses)

    def add_expense(self, expense: Expense) -> None:
        """Adds an expense to the database.

        Args:
            expense (Expense): the expense to add to the database.
        """
        if isinstance(expense, Expense):
            self.expenses.append(expense)
            print(f"{expense} successfully added to ExpenseDatabase")
        else:
            logging.error(
                "TypeError: expense must be an object of class Expense , not %s",
                type(expense),
            )

    def remove_expense(self, expense_id: str) -> None:
        """Removes an expense from the database.

        Args:
            expense_id (str): A unique identifier for an expense.
        """
        if isinstance(expense_id, str):
            self.expenses = [
                expense for expense in self.expenses if expense.id != expense_id
            ] 
            print(f"Expense ID: {expense_id} successfully removed from ExpenseDatabase")
        else:
            logging.error("TypeError: expense_id must be str, not %s", type(expense_id))

    def get_expense_by_id(self, expense_id: str) -> Expense:
        """Retrieves an expense from the database by its unique identifier.

        Args:
            expense_id (str): A unique identifier for an expense.
        """
        if isinstance(expense_id, str):
            for expense in self.expenses:
                if expense.id == expense_id:
                    return expense
            logging.error(
                "Expense ID: %s does not exist in  ExpenseDatabase", expense_id
            )
        else:
            logging.error("TypeError: expense_id must be str, not %s", type(expense_id))

    def get_expense_by_title(self, expense_title: str) -> List:
        """Retrieves a list of expenses from the database by their title.

        Args:
            expense_title (str): The title of the expense.

        Returns:
            List: A list of expenses with the given title.
        """
        if isinstance(expense_title, str):
            return [
                expense for expense in self.expenses if expense.title == expense_title
            ]
        else:
            logging.error(
                "TypeError: expense_title must be str, not %s", type(expense_title)
            )

    def to_dict(self) -> List[Dict]:
        """
        Returns a list of dictionaries representing the expenses in the database.

        Returns:
            List[Dict]: A list of dictionaries representing the expenses in the database.
        """
        return [expense.to_dict() for expense in self.expenses]
