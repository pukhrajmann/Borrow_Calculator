#!/usr/bin/env python
# coding: utf-8

# In[60]:


#This program calcualtes you're total borrowable amount of a portfolio

#Starting Variables
start_invest= 20000
start_loan = 0
borrow_rate = 0.4

#Loop to Calculate final amounts
i = 0
while (i<10):    
    total_loan = start_invest*(borrow_rate)
    loan_sum = total_loan - start_loan
    if(loan_sum >100):
        start_invest = start_invest + loan_sum
        start_loan = total_loan
        i+=1
    else:
        break
equity = start_invest-start_loan
leveraged = 100*start_loan/equity
#Print final invest and final loan amount
print("Total Invested: $", round(start_invest,2))
print("Total Borrowed:$", round(start_loan,2))
print("Equity:$", round(equity,2))
print("Percent Leveraged:",round(leveraged,2),"%")


# In[ ]:




