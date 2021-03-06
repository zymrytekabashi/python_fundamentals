class BankAccount2:
    def __init__(self, int_rate=0, balance = 0): 
        self.int_rate= int_rate
        self.balance=balance
        self.user_account=[]
        
    def account_number(self, acc_number):
        self.user_account.append(acc_number)
        
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if(amount<=self.balance):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
        
    def display_account_info(self):
        print(f" Balance: ${self.balance}")
        return self
	
    def yield_interest(self):
        if self.balance>0:
            self.balance += self.balance*self.int_rate
        else:
            print("You have no money left.")
            
        
        return self
        
a=BankAccount2(0.01)
b=BankAccount2(0.20,10)

a.deposit(100).deposit(200).deposit(50).withdraw(30).yield_interest().display_account_info()
b.deposit(250).deposit(200).withdraw(15).withdraw(100).withdraw(70).withdraw(30).yield_interest().display_account_info()

        
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount2(int_rate=0.02, balance=0)	# added this line
    
        
    def make_deposit(self, amount):
        self.account.balance += amount
        return self
    
    def make_widthdrawal(self, amount):
        self.account.balance -= amount
        return self
    def display_user_balance(self):
        print(f"Name: {self.name} \nBalance: {self.account.balance}")
        return self
        
new_user=User("Zuma","zymryteeek@gmail.com")
new_user.create_account(acc_number=3)
new_user.create_account(acc_number=4)

new_user.make_deposit(100).make_widthdrawal(20).display_user_balance()
