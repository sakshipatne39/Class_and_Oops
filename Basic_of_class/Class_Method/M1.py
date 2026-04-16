cust_data = [

    {
        "cust_name": "cust1",
        "cust_id" : 101,
        "balance" : 200,
        "opening_date" : "25-03-2026",
        "account_type" : "savings"
    },
    {
        "cust_name": "cust2",
        "cust_id" : 105,
        "balance" : 600,
        "opening_date" : "15-03-2026",
        "account_type" : "current"
    }


]

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


        print('cust_details')
        print(f'cust_name := {self.cust_name}')
        print(f'cust_id := {self.cust_id}')
        print(f'balance := {self.balance}')
        print(f'opening_date := {self.opening_date}')
        print(f'account_type := {self.account_type}')


print(cust_data[0])


for cust in cust_data :
    print('customer bank details')
    bank_cust = Bank(cust)
    print('-'*10)
    print('-'*10)