class ATM: 
    def __init__(self, user_pin, initial_balance=0):
        self.user_pin = user_pin
        self.balance = initial_balance
    
    def authenticate(self):
        for _ in range(3):  # Allow up to 3 attempts to enter the correct PIN
            entered_pin = input("Enter your PIN: ")
            if entered_pin == self.user_pin:
                return True
            else:
                print("Incorrect PIN. Please try again.")
        print("Too many incorrect attempts. Exiting.")
        return False
    
    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} has been deposited to your account.")
        else:
            print("Invalid deposit amount. Please try again.")
        self.check_balance()
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn from your account.")
        elif amount > self.balance:
            print("Insufficient funds. Please try again.")
        else:
            print("Invalid withdrawal amount. Please try again.")
        self.check_balance()
    
    def menu(self):
        while True:
            print("\nATM Main Menu:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Please select an option (1-4): ")
            
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter the amount to deposit: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter the amount to withdraw: "))
                self.withdraw(amount)
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    user_pin = "1234"  # The user's PIN (this should be securely stored and encrypted in a real application)
    initial_balance = 1000.00  # The initial balance for the user
    atm = ATM(user_pin, initial_balance)
    
    if atm.authenticate():
        atm.menu()
