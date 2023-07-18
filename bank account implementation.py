#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

account = Account("Ashish", 5000)

print(account.title)  
print(account.balance)

savings_account = SavingsAccount("Ashish", 5000, 5)

print(savings_account.title) 
print(savings_account.balance) 
print(savings_account.interestRate) 


# In[ ]:




