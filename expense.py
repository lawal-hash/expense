from typing import Dict, List
import uuid
from datetime import datetime, timezone


class Expense:
    """
    Expense class to represent an individual financial expense.
    """

    def __init__(self, title: str, amount: float) -> None:
        """
        Args:
            title (str): represents the title of an expense.
            amount (float):  the amount of the expense.
        """
        pass

    def update(self, title: str = None, amount: float = None) -> None:
        """update the title and/or amount of the expense.
        The updated_at attribute should be automatically set
        to the current UTC timestamp whenever an update occurs.

        Args:
            title (str, optional): the title of the expense. Defaults to None.
            amount (float, optional): the amount of the expense. Defaults to None.
        """
        pass

    def to_dict(self) -> Dict:
        """
        Returns:
            Dict: a dictionary representation of the expense.
        """
        pass
