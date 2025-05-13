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
        self.balance += amount
        return self.balance

    def view_balance(self):
        return self.balance


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name):
        init_dep = int(input("Enter initial deposit: "))
        self.accounts[name] = Account(name, init_dep)      
        print(f"Account created for {name} with balance {init_dep:0.1f}")  

    def deposit_money(self, name):
        deposit = int(input("Enter amount to deposit: "))
        new_balance = self.accounts[name].deposit(deposit)
        print(f"{deposit:.1f} deposited. New balance: {new_balance:.1f}")


    def view_balance(self, name):
        print(f"Account holder: {name}, Balance: {self.accounts[name].view_balance():.1f}")

    def run(self):
        while True:
            print("\n1. Create Account\n2. Deposit Money\n3. View Balance\n4. Exit")
            choice = input("Enter choice: ")
            if choice != '4':
                name = input("Enter your name: ")

            if choice == '1':
                self.create_account(name)

            elif choice == '2' and name in self.accounts.keys():
                self.deposit_money(name)

            elif choice == '3' and name in self.accounts.keys():
                self.view_balance(name)
            
            elif choice == '4':
                break

if __name__ == "__main__":
    bank_system = BankSystem()
    bank_system.run()