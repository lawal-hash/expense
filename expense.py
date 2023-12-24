from typing import Dict
from uuid import uuid4
import logging
from datetime import datetime


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
        self.id = str(uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self) -> str:
        return f"Expense(title={self.title}, amount={self.amount})"

    def update(self, title: str = None, amount: float = None) -> None:
        """update the title and/or amount of the expense.
        The updated_at attribute should be automatically set
        to the current UTC timestamp whenever an update occurs.

        Args:
            title (str, optional): the title of the expense. Defaults to None.
            amount (float, optional): the amount of the expense. Defaults to None.
        """
        if title:
            if isinstance(title, str):
                self.title = title
                self.updated_at = datetime.utcnow()
                print(f"Title successfully updated to  {title}")
            else:
                logging.error("TypeError: title must be str, not %s", type(title))

        if amount:
            if isinstance(amount, float):
                self.amount = amount
                self.updated_at = datetime.utcnow()
                print(f"Amount successfully updated to {amount}")
            else:
                logging.error("TypeError: amount must be float, not %s", type(amount))

    def to_dict(self) -> Dict:
        """
        Returns:
            Dict: a dictionary representation of the expense.
        """
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
