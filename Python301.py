class BankApp:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def log(self, transactions):
        with open("transactions.txt", "a") as file:
            file.write (f"{transactions} new balance is {self.balance}\n")

    def withdraw (self, amount):
        if amount > self.balance:
            print("Sorry, you do not have enough funds to withdraw this amount.")
        else:
            amount = float(amount)
        if amount:
            self.balance = self.balance - amount
            self.log(f"Withdrew {amount}")


    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.log(f"Deposeted {amount}")

account = BankApp(50)
while True:
    try:
        action = input("How may we help you today? Type HELP for opetions.")
    except KeyboardInterrupt:
        print("Goodbye")
        break

    if action in ["withdraw", "deposit", "check balance","quit", "HELP"]:
        if action == "withdraw":
            amount = input("How much would you like to withdraw?")
            account.withdraw(amount)
        if action == "deposit":
            amount = input("How much would you like to deposit?")
            account.deposit(amount)
        if action == "quit":
            print("Goodbye")
            break
        if action == "HELP":
            print("You can withdraw, deposit, or check balance")
            
        if action == "check balance":
            pass
        
        
        print(f"Your balance is", account.balance)

        
    
