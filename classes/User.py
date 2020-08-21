class User:		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0
        

     
    def make_deposit(self, amount):
        self.account_balance+=amount
        return self 
            
     
    def make_withdrawal(self, amount):
        self.account_balance -=amount
        return self
    
    def transfer_money(from_user, to_user, amount):
        from_user.make_withdrawal(amount)
        to_user.make_deposit(amount)
        print("Account balance of the first user is: " + str(from_user.account_balance))
        print("Account balance of the second user is: " + str(to_user.account_balance))
        
            
    def display_user_balance(self):
        print(self.name + " " + str(self.account_balance))
        return self
        
a=User()
b=User()
c=User()
    
a.make_deposit(100).make_deposit(150).make_deposit(50).make_withdrawal(30).display_user_balance()


b.make_deposit(40).make_deposit(180).make_withdrawal(20).make_withdrawal(60).display_user_balance()


c.make_deposit(500).make_withdrawal(30).make_withdrawal(100).make_withdrawal(80).display_user_balance().transfer_money( b, 100)

    
    
        