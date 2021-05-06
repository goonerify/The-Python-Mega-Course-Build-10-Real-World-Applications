class Account:
    def __init__(self, filepath) -> None:
        # Create an "instance variable" for filepath
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount
        self.commit()

    def deposit(self, amount):
        self.balance=self.balance + amount
        self.commit()

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class CheckingAccount(Account):
    def __init__(self, filepath, fee) -> None:
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee


# account=Account("account//balance.txt")
# print(account.balance)
# account.withdraw(100)
# print(account.balance)
# account.deposit(200)
# print(account.balance)

checking=CheckingAccount("account//balance.txt", 1)
checking.transfer(40)
print(checking.balance)
checking.commit()
