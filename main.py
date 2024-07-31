from abc import ABC, abstractmethod
""" Open-Closed Principle """


class Transaction(ABC):
    def __init__(self, customerId, tellerId):
        self.customerId = customerId
        self.tellerId = tellerId

    def get_customer_id(self):
        return self.customerId
    
    def get_teller_id(self):
        return self.tellerId
    
    @abstractmethod
    def get_transaction_description(self):
        pass


class Deposit(Transaction):
    def __init__(self, customerId, tellerId, amount):
        super().__init__(customerId, tellerId)
        self.amount = amount
    
    def get_transaction_description(self):
        return f'Teller {self.get_teller_id()} deposited {self.amount} to account {self.get_customer_id()}' 

class Withdrawal(Transaction):
    def __init__(self, customerId, tellerId, amount):
        super().__init__(customerId, tellerId)
        self.amount = amount

    def get_transaction_description(self):
        return f'Teller {self.get_teller_id()} withdrew {self.amount} from account {self.get_customer_id()}'
    
class OpenAccount(Transaction):
    def __init__(self, customerId, tellerId):
        super().__init__(customerId, tellerId)

    def get_transaction_description(self):
        return f'Teller {self.get_teller_id()} opened account {self.get_customer_id()}'
        

class BankTeller:
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id
    
class BankAccount:
    def __init__(self, customerId, name, balance):
        self.customerId = customerId
        self.name = name
        self.balance = balance
    
    def get_balance(self):

        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

class BankSystem:
    def __init__(self, accounts, transactions):
        self.accounts = accounts
        self.transactions = transactions

    def get_account(self, customerId):
        return self.accounts[customerId]
    
    def get_accounts(self):
        return self.accounts
    
    def get_transactions(self):
        return self.transactions
    
    def open_account(self, customer_name, teller_id):
        # Create Account
        customerId = len(self.get_accounts())
        account = BankAccount(customerId, customer_name, 0)
        self.accounts.append(account)

        # Log Transaction
        transaction = OpenAccount(customerId, teller_id)
        self.transactions.append(transaction)
        return customerId
    
    def deposit(self, customer_id, teller_id, amount):
        account = self.get_account(customer_id)
        account.deposit(amount)

        transaction = Deposit(customer_id, teller_id, amount)
        self.transactions.append(transaction)

    def withdraw(self, customer_id, teller_id, amount):
        if amount > self.get_account(customer_id).get_balance():
            raise Exception("Insufficient funds")
        account = self.get_account(customer_id)
        account.withdraw(amount)

        transaction = Withdrawal(customer_id, teller_id, amount)
        self.transactions.append(transaction)



import random

class BankBranch:
    def __init__(self, address, cash_on_hand, bank_system):
        self.address = address
        self.cash_on_hand = cash_on_hand
        self.bank_system = bank_system
        self.tellers = []

    def add_teller(self, teller):
        self.tellers.append(teller)

    def get_available_teller(self):
        index = round(random.random() * (len(self.tellers) -1))
        return self.tellers[index].get_id()
    
    def open_account(self, customer_name):
        if not self.tellers:
            raise ValueError("Branch does not have any tellers")
        teller_id = self.get_available_teller()
        return self.bank_system.open_account(customer_name, teller_id)

    def deposit(self, customer_id, amount):
        if not self.tellers:
            raise ValueError("Brand does not have any tellers")
        teller_id = self.get_available_teller()
        self.bank_system.deposit(customer_id, teller_id, amount)

    def withdraw(self, customer_id, amount):
        if amount > self.cash_on_hand:
            raise ValueError('Branch does not have enough cash')
        if not self.tellers:
            raise ValueError('Branch does not have any tellers')
        self.cash_on_hand += amount
        teller_id = self.get_available_teller()
        self.bank_system.withdraw(customer_id, teller_id, amount)

    def collect_cash(self, ratio):
        cash_to_collect = round(self.cash_on_hand * ratio)
        self.cash_on_hand -= cash_to_collect
        return cash_to_collect
    
    def provide_cash(self, amount):
        self.cash_on_hand += amount

class Bank:
    def __init__(self, branches, bank_system, total_cash):
        self.branches = branches
        self.bank_system = bank_system
        self.total_cash = total_cash

    def add_branch(self, address, initial_funds):
        branch = BankBranch(address, initial_funds, self.bank_system)
        self.branches.append(branch)
        return branch
    
    def collect_cash(self, ratio):
        for branch in self.branches:
            cash_collected = branch.collect_cash(ratio)
            self.total_cash += cash_collected

    def print_transactions(self):
        for transaction in self.bank_system.get_transactions():
            print(transaction.get_transaction_description())

bankSystem = BankSystem([], [])
bank = Bank([], bankSystem, 10000)

branch1 = bank.add_branch('123 Main St', 1000)
branch2 = bank.add_branch('456 Elm St', 1000)

branch1.add_teller(BankTeller(1))
branch1.add_teller(BankTeller(2))
branch2.add_teller(BankTeller(3))
branch2.add_teller(BankTeller(4))

customerId1 = branch1.open_account('John Doe')
customerId2 = branch1.open_account('Bob Smith')
customerId3 = branch2.open_account('Jane Doe')

branch1.deposit(customerId1, 100)
branch1.deposit(customerId2, 200)
branch2.deposit(customerId3, 300)

branch1.withdraw(customerId1, 50)
""" Possible Output:
    Teller 1 opened account 0
    Teller 2 opened account 1
    Teller 3 opened account 2
    Teller 1 deposited 100 to account 0
    Teller 2 deposited 200 to account 1
    Teller 4 deposited 300 to account 2
    Teller 2 withdrew 50 from account 0
"""

bank.print_transactions()


