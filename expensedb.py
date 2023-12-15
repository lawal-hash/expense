from typing import Dict, List
from expense import Expense


class ExpenseDatabase:
    """
    Manages a collection of Expense objects
    """

    def __init__(self) -> None:
        pass

    def add_expense(self, expense: Expense) -> None:
        """Adds an expense to the database.

        Args:
            expense (Expense): the expense to add to the database.
        """
        pass

    def remove_expense(self, expense_id: str) -> None:
        """Removes an expense from the database.

        Args:
            expense_id (str): A unique identifier for an expense.
        """
        pass

    def get_expense_by_id(self, expense_id: str) -> None:
        """Retrieves an expense from the database by its unique identifier.

        Args:
            expense_id (str): A unique identifier for an expense.
        """
        pass

    def get_expense_by_title(self, expense_title: str) -> List:
        """Retrieves a list of expenses from the database by their title.

        Args:
            expense_title (str): The title of the expense.

        Returns:
            List: A list of expenses with the given title.
        """
        pass

    def to_dict(self) -> List[Dict]:
        """
        Returns a list of dictionaries representing the expenses in the database.

        Returns:
            List[Dict]: A list of dictionaries representing the expenses in the database.
        """
        pass
