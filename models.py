class Wallet:
    def __init__(self, user):
        self.user = user
        self.naira_balance = 50000 #just for testing
        self.usdt_balance = 100

    def send(self, amount):
        # We will adding encryption later
        print("Sending {amount}")
        self.naira_balance = int(amount)

    def convert_naira_to_usdt(self, naira_amount):
        rate = 1600
        usdt = naira_amount / rate
        self.naira_balance -= naira_amount
        self.usdt_balance += usdt 
        return usdt