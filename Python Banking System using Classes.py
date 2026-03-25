#!/usr/bin/env python
# coding: utf-8

# # Create a class to handle Bank transactions and display the details of   transactions.

# In[1]:


class BankAccount:
    
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def display_details(self):
        print("\nAccount Holder:", self.name)
        print("Current Balance:", self.balance)
        print("Transactions:")
        for t in self.transactions:
            print("-", t)


# Using the class
acc = BankAccount("Chanda", 1000)

acc.deposit(500)
acc.withdraw(300)
acc.withdraw(1500) 

acc.display_details()


# In[ ]:




