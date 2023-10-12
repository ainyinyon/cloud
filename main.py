class FamilyMember:
    def __init__(self, name, earning_status=True, earnings=0):
        self.name = name
        self.earning_status = earning_status
        self.earnings = earnings

    def __str__(self):
        return f"Name: {self.name}, Earning Status: {'Earning' if self.earning_status else 'Not Earning'}, " \
               f"Earnings: {self.earnings}"
    
class Expense:
    def __init__(self, value, category, description):
        self.value = value
        self.category = category
        self.description = description

    def __str__(self):
        return f"Value: {self.value}, Category: {self.category}, Description: {self.description}"


class FamilyExpenseTracker:
    def __init__(self):
        self.members = []
        self.expense_list = []

    def add_family_member(self, name, earning_status=True, earnings=0):
        if not name.strip():
            raise ValueError("Name field cannot be empty")

        member = FamilyMember(name, earning_status, earnings)
        self.members.append(member)

    def update_family_member(self, member, earning_status=True, earnings=0):
        if member:
            member.earning_status = earning_status
            member.earnings = earnings

    def calculate_total_earnings(self):
        total_earnings = sum(member.earnings for member in self.members if member.earning_status)
        return total_earnings
    
    def add_expense(self, value, category, description):
        if value == 0:
            raise ValueError("Value cannot be zero")
        if not category.strip():
            raise ValueError("Please choose a category")
        
        expense = Expense(value, category, description)
        self.expense_list.append(expense)

    def calculate_total_expenditure(self):
        total_expenditure = sum(expense.value for expense in self.expense_list)
        return total_expenditure

    def deduct_expenses(self, expenses):
        total_earnings = self.calculate_total_earnings()
        total_expenditure = self.calculate_total_expenditure()
        remaining_balance = total_earnings - total_expenditure
        return remaining_balance


if __name__ == "__main__":
    expense_tracker = FamilyExpenseTracker()

