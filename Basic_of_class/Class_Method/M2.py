
cust1 = {

     "cust_name": "cust1",
        "cust_id" : 101,
        "balance" : 200,
        "opening_date" : "25-03-2026",
        "account_type" : "savings"
}



class Bank:
    cust_name = ' '
    cust_id = 0
    balance = 0        
    opening_date = ' '
    account_type = ' '     

# def_init__(self, cust_name, cust_id, balance, opening_date, account_type):

    def __init__(self, custdata):
        self.cust_name = custdata.get('cust_name')
        self.cust_id = custdata.get('cust_id')
        self.balance = custdata.get('balance')
        self.opening_date = custdata.get('opening_date')    
        self.account_type = custdata.get('account_type')

    def deposite(self,amt):
        print(f"acc number : {self.cust_id} deposited with {amt} amount")
        self.balance = self.balance + amt

    def withdraw(self, amt):
        print(f"acc number : {self.cust_id} withdrew {amt} amount")
        self.balance = self.balance - amt

    def getcustDetails(self):
        print('-'*10)
        print('cust_details')
        print(f'cust_name := {self.cust_name}')
        print(f'cust_id := {self.cust_id}')
        print(f'balance := {self.balance}')
        print(f'opening_date := {self.opening_date}')
        print(f'account_type := {self.account_type}')
        print('-'*10)


c1 = Bank(cust1)

c1.getcustDetails()

c1.deposite(100)

c1.getcustDetails()

c1.withdraw(50)

c1.getcustDetails()