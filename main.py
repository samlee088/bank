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
        return f'Teller {self.get_teller_id()} deposited {self._amount} to account {self.get_customer_id()}' 

class Withdrawal(Transaction):
    def __init__(self, customerId, tellerId, amount):
        super().__init__(customerId, tellerId)
        self.amount = amount

    def get_transaction_description(self):
        return f'Teller {self.get_teller_id()} withdrew {self._amount} from account {self.get_customer_id()}'
    
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
        customerId = len(self.getAccounts())
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
