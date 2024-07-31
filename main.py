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
    
