from cmath import nan


customer_name = input("Welcome, what is your name? ")
starting_balance = 5000.2
expenditure_item = "banjo"
expenditure = 0
deposits = 0
expense_amount = 0
expense_item = nan
user_name = nan
balance = 0


def start_function(the_name, the_balance):
    global deposits, expenditure
    print (f"Hello {the_name} your starting balance is {the_balance}")
    deposits = float(input(f"How much of your pay check would you like to deposit?"))
    expenditure_item = input(f"Looks like you went shopping. What did you buy?")
    expenditure = float(input(f"How much does a {expenditure_item} cost: "))

def checking_balance(user_name, balance, deposits, expense_item, expense_amount):
     ending_balance = (balance) + (deposits) - (expense_amount)
     print(f"Good day, {customer_name}. After speding money on a {expenditure_item} in the amount of {expenditure}, your current checking balance is: {ending_balance}")

start_function(customer_name, starting_balance,)    
checking_balance(user_name, balance, deposits, expense_item, expense_amount)