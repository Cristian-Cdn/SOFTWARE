from account import Account

class Driver(Account):
    def _init_(self, name, document, email, password):
        super()._init_(name, document, email, password)