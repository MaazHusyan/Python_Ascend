from abc import ABC
# class and object 
class Deposit:
    def deposit(self, amount):
        self._balance += amount
        print(f"{amount} is deposited in your bank account.")

class Withdraw:
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"{amount} is withdrawn from your bank account.")
        else:
            print("Insufficient funds")
            
class BankAccount(Deposit, Withdraw): #<== Inheritence
    def __init__(self,accouny_holder, balance) -> None:
        self.account_holder = accouny_holder
        self._balance = balance #<== Encapsulation
        
    def check_balance(self):
        print(f"{self.account_holder}, Your current balance is {self._balance}")


class SavingAccount(BankAccount):
    def __init__(self, accouny_holder, balance, interest_per_rate) -> None:
        super().__init__(accouny_holder, balance)
        self.interest_per_rate = interest_per_rate
        self.withdraw_count = 0
    
    def withdraw(self, amount):
        if self.withdraw_count >= 3:
            print(f"Withdraw limit exceeded for this month,")
            return
        super().withdraw(amount)
        self.withdraw_count += 1
        
    def apply_interest(self):
        interest = self._balance /100 * self.interest_per_rate
        
        print(f"%{self.interest_per_rate} interest applied on {self._balance},")
        
        self._balance += interest
        
        print(f"Interest amount: {interest}")
        
class CurrentAccount(BankAccount): # <=== Inheritance 
    def __init__(self, accouny_holder, balance, min_balance) -> None:
        super().__init__(accouny_holder, balance)
        self.min_balance = min_balance
    
    def withdraw(self, amount):
        if self._balance - amount < self.min_balance:
            print(f"Can't withdraw: You must keep minimum balance of {self.min_balance}")
        else:
            super().withdraw(amount)


c_a = CurrentAccount("maaz",3000,2100)

c_a.withdraw(2000)