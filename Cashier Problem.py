#!/usr/bin/env python
# coding: utf-8

# In[2]:


def calculate_notes(amt):
    total_100 = amt // 100
    amt = amt % 100

    total_50 = amt // 50
    amt = amt % 50

    total_10 = amt // 10

    print("100 notes:", total_100)
    print("50 notes:", total_50)
    print("10 notes:", total_10)


amt = int(input("Enter Your Amount = "))
calculate_notes(amt)


# In[ ]:




