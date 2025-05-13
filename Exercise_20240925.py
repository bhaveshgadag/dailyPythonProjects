# Create a basic console-based banking system where users can:
# Create accounts
# Deposit money
# View balance
# Exit the system.

class Account:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit

    def deposit(self, amount):
        ...

    def view_balance(self):
        ...


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        name = input("Enter your name: ")
        init_dep = int(input("Enter initial deposit: "))
        self.accounts[name] = Account(name, init_dep)      
        print(f"Account created for {name} with balance {init_dep:0.1f}")  

    def deposit_money(self):
        ...


    def view_balance(self):
        ...
       

    def run(self):
        while True:
            print("\n1. Create Account\n2. Deposit Money\n3. View Balance\n4. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.create_account()

            elif choice == '2':
                self.deposit_money()

            elif choice == '3':
                self.view_balance()

            elif choice == '4':
                break


if __name__ == "__main__":
    bank_system = BankSystem()
    bank_system.run()