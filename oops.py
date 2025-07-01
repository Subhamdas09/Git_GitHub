class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balence -= amount
        print("Rs", amount, "was debited")
        print("total balence =", self.get_balence)

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("total balence =", self.get_balence)

    def get_balence(self):
        return self.balence
    

acc1 = Account(10000, 1001)
acc1.credit(4000) 

