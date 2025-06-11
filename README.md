# Personal Expense Tracker

This is a simple interactive command line application in python for tracking personal expenses, setting a monthly budget, and saving or loading expenses from a CSV file. 

# Features: 

  * Add new expenses with date, category, amount, and description
  * View all recorded expenses in a readable format
  * Set a custom monthly budget
  * Track how much of your budget has been spent and what remains
  * Save your expenses to a CSV file
  * Load previously saved expenses from the CSV file automatically on startup

# Requirements: 

  * Python 3.6+
  * No external libraries required

# How to run: 
1. Clone the repository or copy the script to your local machine
2. Open a terminal and navigate to the project directory
3. Run the program using:
   
   <pre> python expense_tracker.py </pre>
  
5. Follow the on screen menu options to interact with the app

# How it works: 

  * Expenses are stored in a list of dictionaries
  * Data is loaded from and saved to a CSV file name expenses.csv
  * The budget is user defined and compared against the total expenses for basic tracking

# Example: 
  <pre>
    Personal Expense Tracker 
    1. Add Expense 
    2. View Expenses 
    3. Set monthly budget 
    4. Track budget 
    5. Save expenses 
    6. Exit 
    Choose an option (1-6): 
  </pre>

# Notes: 
  All expenses are stored locally in expenses.csv. Ensure you save your expenses before existing if you want them to persist. The program automatically loads saved expenses if the file exists. 

# Possible improvements: 
  * Category-based filtering or analysis
  * Monthly report generation
  * GUI version with Tkinter or PyQt
  * Export to PDF or Excel
  * Password protection or user profiles
