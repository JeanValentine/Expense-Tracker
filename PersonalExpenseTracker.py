import csv #For reading and writing CSV files. A CVS file is a text file that uses commmas to seperate values.  
import os # Checks if the file exists or not 
from datetime import datetime # Handles date and time operations 
from typing import List, Dict, Any 

''' This is used for type hinting. Type hinting is a way to 
describe the expected data types of varibles, function parameters, and return values ''' 

#Type alias: 
 
Expense = Dict[str, Any] 

''' An expense is a dictionary with string keys and values of any type of value. '''

class ExpenseTracker:
    def __init__(self):
        self.expenses: List[Expense] = [] #This will list all the expenses 
        self.budget: float = 0.0 # This will hold the users budget 
        self.load_expenses() # And this will load the expenses from the CSV file if its available

    #Adding an expense 

    def add_expense(self): #Stores the expense in a dictionary 
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        category = input("Enter the category of the expense: ")
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description of the expense: ")

        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }

        self.expenses.append(expense) #this appends the expense to the expenses list 
        print("Expense added successfully.") 

    # View all recorded expenses: 

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.") #notifying the user that there are no expenses recorded 
            return 

        for expense in self.expenses: 
            if all(key in expense for key in ['date', 'category', 'amount', 'description']): 
                print(f"Date: {expense['date']}, Category: {expense['category']}, " 
                      f"Amount: {expense['amount']}, Description: {expense['description']}")
            else: # this check if all the keys are presenst in the expense dictionary 
                print("Incomplete expense entry, skipping...")

    # Setting users monthly budget: 

    def set_budget(self):
        try:
            self.budget = float(input("Enter your monthly budget: "))
            print(f"Monthly budget set to: {self.budget}")
        except ValueError: # This will catch any errors that occur if the user enter an invalid value 
            print("Invalid input. Please enter a numeric value for the budget.")

    #tracking the budget: 

    def track_budget(self):
        total_expenses = sum(expense['amount'] for expense in self.expenses) #computing the sum of all expenses 
        print(f"Total expenses so far: {total_expenses}") 

        if total_expenses > self.budget: #comparing the total expenses to the users budget 
            print("You have exceeded your budget!")
        else:
            remaining_balance = self.budget - total_expenses
            print(f"You have {remaining_balance} left for the month.")

    #Saving the expenses to a CVS file: 

    def save_expenses(self):
        with open('expenses.csv', 'w', newline='') as csvfile: #open file expenses.csv
            fieldnames = ['date', 'category', 'amount', 'description'] # these are our headers 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames) #writes each expense as a row in the CSV 

            writer.writeheader()
            for expense in self.expenses:
                writer.writerow(expense)

        print("Expenses saved to expenses.csv.")

    #:Loading expenses from the CSV file: 

    def load_expenses(self):
        if os.path.exists('expenses.csv'):
            with open('expenses.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.expenses.append({
                        'date': row['date'],
                        'category': row['category'],
                        'amount': float(row['amount']),
                        'description': row['description']
                    })
            print("Expenses loaded from expenses.csv.")
        else:
            print("No previous expenses found.")

            '''This checks if expenses.csv exists or not using the os.path.exists() method. 
            If it does exist, then it opens the file and reads off the expenses 
            and adds them to the expense list. '''

    # The diplay menu function to show the user the options available: 

    def display_menu(self):
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Monthly Budget")
        print("4. Track Budget")
        print("5. Save Expenses")
        print("6. Exit")

    #Main application loop:

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option (1-6): ")

            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.set_budget()
            elif choice == '4':
                self.track_budget()
            elif choice == '5':
                self.save_expenses()
            elif choice == '6':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

'''This is an infinite loop that will keep the program runing until the user chooses to exit by 
entering '6'. The user can choose to either add an expense, view expenses, set a specific budget,
track that very budget, save the expenses to a CSV file, or as we said before, exit the program. '''

# Now we have out entry point for the program: 

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
    '''Initiates the ExpenseTracker class and starts the application loop '''