from datetime import datetime


class Expense:
    def __init__(self, amount, category, date_str):
        self.amount = amount
        self.category = category

        try:
            self.date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")
