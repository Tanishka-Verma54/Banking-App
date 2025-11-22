import sys

INITIAL_BALANCE = 500.00
MIN_WITHDRAWAL = 0.01
LOAN_ANNUAL_RATE = 0.12

class BankAccount:
    def __init__(self, holder_name, initial_deposit=INITIAL_BALANCE):
        self.account_holder = holder_name
        if initial_deposit >= 0:
            self.balance = round(initial_deposit, 2)
        else:
            self.balance = 0.00
            print(f"Initial deposit cannot be negative. Setting balance to ₹0.00 for {holder_name}.")   
        print(f" Account created for {self.account_holder} with an initial balance of ₹{self.balance:.2f}.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += round(amount, 2)
            print(f"\n Deposit successful! Added ₹{amount:.2f}.")
            self.check_balance()
            return True
        else:
            print("\n Invalid deposit amount. Must be positive.")
            return False

    def withdraw(self, amount):
        amount = round(amount, 2)
        if amount < MIN_WITHDRAWAL:
            print(f"\n Invalid withdrawal amount. Must be at least ₹{MIN_WITHDRAWAL:.2f}.")
            return False
        if self.balance >= amount:
            self.balance -= amount
            print(f"\n Withdrawal successful! Withdrew ₹{amount:.2f}.")
            self.check_balance()
            return True
        else:
            print(f"\n Insufficient funds! You tried to withdraw ₹{amount:.2f}.")
            self.check_balance()
            return False

    def take_loan(self, principal, years):
        if principal <= 0 or years <= 0:
            print("\n Invalid loan parameters. Both principal amount and duration must be positive.")
            return None 
        monthly_rate = LOAN_ANNUAL_RATE / 12
        num_payments = years * 12 
        power_term = (1 + monthly_rate) ** num_payments 
        numerator = principal * monthly_rate * power_term
        denominator = power_term - 1
        if denominator == 0:
            print("Error in loan calculation (denominator is zero).")
            return None   
        monthly_installment = round(numerator / denominator, 2)

        print("\n--- LOAN CALCULATION RESULT ---")
        print(f"Loan Principal: ₹{principal:.2f}")
        print(f"Annual Interest Rate: {LOAN_ANNUAL_RATE * 100:.0f}%")
        print(f"Loan Duration: {years} years ({num_payments} months)")
        print(f"Your fixed monthly installment (EMI) will be: ₹{monthly_installment:.2f}")
        print("-"*50) 
        return monthly_installment

    def check_balance(self):
        print(f" Current balance for {self.account_holder}: ₹{self.balance:.2f}")

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ₹{self.balance:.2f}"

def get_valid_amount(prompt, allow_zero=False):
    while True:
        amount_str = input(prompt).strip()
        if amount_str.lower() in ('q', 'quit', 'exit'):
            return None
        amount = float(amount_str)
        if amount > 0 or (allow_zero and amount >= 0):
            return amount
        elif amount == 0 and allow_zero:
             return amount
        else:
            print("Amount must be positive.")

def get_valid_integer(prompt):
    while True:
        value_str = input(prompt).strip()    
        if value_str.lower() in ('q', 'quit', 'exit'):
            return None 
        value = int(value_str)
        if value > 0:
            return value
        else:
            print("Duration must be a positive whole number.")
        
def main_app():
    print("="*50)
    print("      Welcome to the Banking App!")
    print("="*50)
    holder_name = input("Welcome! Please enter your name to open an account: ").strip()
    print("\n--- ACCOUNT CREATION ---")
    initial_deposit = get_valid_amount("Enter initial deposit amount (0.00 or higher): ₹", allow_zero=True)
    if initial_deposit is None:
        print("Application exiting during account setup.")
        sys.exit()        
    account = BankAccount(holder_name, initial_deposit)
    while True:
        print("-"*50)
        print("Choose an operation:")
        print("1: Deposit Money")
        print("2: Withdraw Money")
        print("3: Check Balance")
        print("4: Take Loan (EMI Calculator)")
        print("5: Exit Application")
        print("-"*50)
    
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            print("\n--- DEPOSIT ---")
            deposit_amount = get_valid_amount("Enter amount to deposit (or 'q' to cancel): ₹")
            if deposit_amount is not None:
                account.deposit(deposit_amount)
        elif choice == '2':
            print("\n--- WITHDRAW ---")
            withdraw_amount = get_valid_amount("Enter amount to withdraw (or 'q' to cancel): ₹")
            if withdraw_amount is not None:
                account.withdraw(withdraw_amount) 
        elif choice == '3':
            print("\n--- BALANCE ---")
            account.check_balance()
        elif choice == '4':
            print("\n--- LOAN CALCULATION ---")
            loan_amount = get_valid_amount("Enter the principal loan amount: ₹")
            if loan_amount is not None:
                loan_years = get_valid_integer("Enter loan duration in full years: ")
                if loan_years is not None:
                    account.take_loan(loan_amount, loan_years)  
        elif choice == '5':
            print("\n=========================================")
            print(f"Thank you for banking with us, {account.account_holder}! Have a great day.")
            print(f"Final Account Summary: {account}")
            print("=========================================")
            break 
        else:
            print(" Invalid choice. Please enter a number between 1 and 5.")
            
if __name__ == "__main__":
    main_app()