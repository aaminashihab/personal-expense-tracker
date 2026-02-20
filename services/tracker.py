import numpy as np


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def calculate_total(self, expenses=None):
        if expenses is None:
            expenses = self.expenses

        return sum(exp.amount for exp in expenses)

    def category_wise_total(self):
        totals = {}

        for exp in self.expenses:
            totals[exp.category] = totals.get(exp.category, 0) + exp.amount

        return totals

    def highest_spending_category(self):
        totals = self.category_wise_total()

        if not totals:
            return None, 0

        highest = max(totals, key=totals.get)
        return highest, totals[highest]

    def percentage_analysis(self):
        totals = self.category_wise_total()

        if not totals:
            return {}

        values = np.array(list(totals.values()))
        total = np.sum(values)

        if total == 0:
            return {}

        percentages = (values / total) * 100
        categories = list(totals.keys())

        return dict(zip(categories, percentages))

    def monthly_summary(self, month, year):
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")

        return [
            exp for exp in self.expenses
            if exp.date.month == month and exp.date.year == year
        ]
