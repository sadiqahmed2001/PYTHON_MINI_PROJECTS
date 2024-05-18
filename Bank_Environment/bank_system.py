# import os

# class User:
#     def __init__(self, username='', date=0, month=0, year=0, pnumber='', adharnum='', fname='', lname='', fathname='', mothname='', address='', typeaccount=''):
#         self.username = username
#         self.date = date
#         self.month = month
#         self.year = year
#         self.pnumber = pnumber
#         self.adharnum = adharnum
#         self.fname = fname
#         self.lname = lname
#         self.fathname = fathname
#         self.mothname = mothname
#         self.address = address
#         self.typeaccount = typeaccount

# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def account():
#     clear_screen()
#     print("!!!!!CREATE ACCOUNT!!!!!")
#     user = User()
#     user.fname = input("\nFIRST NAME: ")
#     user.lname = input("\nLAST NAME: ")
#     user.fathname = input("\nFATHER's NAME: ")
#     user.mothname = input("\nMOTHER's NAME: ")
#     user.address = input("\nADDRESS: ")
#     user.typeaccount = input("\nACCOUNT TYPE: ")
#     user.date = int(input("\nDATE OF BIRTH - DATE: "))
#     user.month = int(input("\nDATE OF BIRTH - MONTH: "))
#     user.year = int(input("\nDATE OF BIRTH - YEAR: "))
#     user.adharnum = input("\nADHAR NUMBER: ")
#     user.pnumber = input("\nPHONE NUMBER: ")
#     user.username = input("\nUSERNAME: ")
#     user.password = input("\nPASSWORD: ")

#     with open("users.txt", "a") as file:
#         file.write(f"{user.username},{user.password},{user.fname},{user.lname},{user.fathname},{user.mothname},{user.address},{user.typeaccount},{user.date}-{user.month}-{user.year},{user.adharnum},{user.pnumber}\n")
    
#     print("\nAccount created successfully!")
#     input("Press Enter to continue...")

# def account():
#     name = input("Enter your name: ")
#     account_number = input("Enter your account number: ")
#     balance = float(input("Enter your initial balance: "))
#     new_account = account(name, account_number, balance)
#     save_account(new_account)
#     print("Account created successfully!")

# def save_account(account):
#     filename = "accounts.txt"
#     with open(filename, "a") as file:
#         file.write(f"{account.name},{account.account_number},{account.balance}\n")

# def transfermoney():
#     sender_account_number = input("Enter your account number: ")
#     receiver_account_number = input("Enter the receiver's account number: ")
#     amount = float(input("Enter the amount to transfer: "))
#     transfer_funds(sender_account_number, receiver_account_number, amount)

# def transfer_funds(sender_account_number, receiver_account_number, amount):
#     sender_account = load_account(sender_account_number)
#     receiver_account = load_account(receiver_account_number)
#     if sender_account and receiver_account:
#         if sender_account.balance >= amount:
#             sender_account.balance -= amount
#             receiver_account.balance += amount
#             update_account(sender_account)
#             update_account(receiver_account)
#             print("Transfer successful!")
#         else:
#             print("Insufficient balance.")
#     else:
#         print("One or both accounts not found.")

# def update_account(account):
#     filename = "accounts.txt"
#     accounts = []
#     with open(filename, "r") as file:
#         for line in file:
#             name, acc_num, balance = line.strip().split(",")
#             if acc_num != account.account_number:
#                 accounts.append(line.strip())
#             else:
#                 accounts.append(f"{account.name},{account.account_number},{account.balance}")
#     with open(filename, "w") as file:
#         for account_info in accounts:
#             file.write(account_info + "\n")

# def checkbalance():
#     account_number = input("Enter your account number: ")
#     account = load_account(account_number)
#     if account:
#         print(f"Your current balance is: {account.balance}")
#     else:
#         print("Account not found.")

# def load_account(account_number):
#     filename = "accounts.txt"
#     if os.path.isfile(filename):
#         with open(filename, "r") as file:
#             for line in file:
#                 name, acc_num, balance = line.strip().split(",")
#                 if acc_num == account_number:
#                     return Account(name, acc_num, float(balance))
#     return None

# def login():
#     clear_screen()
#     print("ACCOUNT LOGIN")
#     username = input("\nUSERNAME: ")
#     password = input("\nPASSWORD: ")

#     with open("users.txt", "r") as file:
#         for line in file:
#             user_data = line.split(",")
#             if user_data[0] == username and user_data[1] == password:
#                 print("\nLogin successful!")
#                 input("Press Enter to continue...")
#                 return
#     print("\nInvalid username or password.")
#     input("Press Enter to continue...")

# def main():
#     while True:
#         clear_screen()
#         print("WELCOME TO CHAMAN BANK ACCOUNT SYSTEM PVT.LTD INDIA\n")
#         print("**********************************")
#         print("DEVELOPER- Sadiq Ahmed\n\n")
#         print("1. CREATE A BANK ACCOUNT")
#         print("2. ALREADY A USER? SIGN IN")
#         print("3. EXIT\n\n")
#         choice = input("ENTER YOUR CHOICE: ")

#         if choice == '1':
#             account()
#         elif choice == '2':
#             login()
#         elif choice == '3':
#             clear_screen()
#             print("Thank you for using our system. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter again.")
#             input("Press Enter to continue...")

# if __name__ == "__main__":
#     main()



import json

def create_bank_account():
    print("Welcome to Bank Account Creation!")

    # Get user input
    name = input("Enter your name: ")
    account_number = input("Enter your account number: ")
    balance = float(input("Enter your initial balance: "))
    account_type = input("Enter your account type (Savings/Current): ")

    # Create a dictionary to store the account details
    account_details = {
        "Name": name,
        "Account Number": account_number,
        "Balance": balance,
        "Account Type": account_type,
        "Transfer Records": []
    }

    # Write the account details to a file
    with open("bank_accounts.txt", "a") as file:
        file.write(json.dumps(account_details) + '\n')

    print("Bank Account created successfully!")

def transfer_money(sender_name, receiver_name, amount):
    sender_found = False
    receiver_found = False

    # Read account details from the file
    with open("bank_accounts.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            account = json.loads(line)

            if account["Name"] == sender_name:
                sender_found = True
                if account["Balance"] >= amount:
                    account["Balance"] -= amount
                    account["Transfer Records"].append({"Recipient": receiver_name, "Amount": amount})
                else:
                    print("Insufficient balance in the sender's account.")
                    return

            if account["Name"] == receiver_name:
                receiver_found = True
                account["Balance"] += amount

            file.write(json.dumps(account) + '\n')

        if not sender_found:
            print("Sender's account not found.")
        if not receiver_found:
            print("Receiver's account not found.")

    print("Money transfer successful.")

def check_balance(username):
    user_found = False

    # Read transfer records from the file
    with open("bank_accounts.txt", "r") as file:
        for line in file:
            account = json.loads(line)
            if account["Name"] == username:
                user_found = True
                print(f"Balance for {username}: ${account['Balance']:.2f}")
                # Assuming transfer records are stored in the account dictionary
                if "Transfer Records" in account:
                    print("Transfer Records:")
                    for record in account["Transfer Records"]:
                        print(f"Transfer to {record['Recipient']}: ${record['Amount']:.2f}")
                else:
                    print("No transfer records found for this account.")
                break

    if not user_found:
        print("User not found in the records.")

def login(username):
    # Check if the username exists in the records
    with open("bank_accounts.txt", "r") as file:
        for line in file:
            account = json.loads(line)
            if account["Name"] == username:
                print("Login successful!")
                return True
    print("Invalid username. Please try again.")
    return False

if __name__ == "__main__":
    while True:
        print("\nWelcome to the Bank!\n")
        print("1. Create Bank Account")
        print("2. Transfer Money")
        print("3. Check Balance")
        print("4. Login")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_bank_account()
        elif choice == '2':
            sender_name = input("Enter your username: ")
            receiver_name = input("Enter the recipient's username: ")
            amount = float(input("Enter the amount to transfer: "))
            transfer_money(sender_name, receiver_name, amount)
        elif choice == '3':
            username = input("Enter your username: ")
            check_balance(username)
        elif choice == '4':
            username = input("Enter your username: ")
            login(username)
        elif choice == '5':
            print("Thank you for using the Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")








