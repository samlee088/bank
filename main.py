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