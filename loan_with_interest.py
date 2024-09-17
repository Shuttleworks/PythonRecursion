# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:14:31 2024

@author: Shuttleworks

An exercise in recursion to illustrate how long it would take to pay off a credit card debt if only the
minimum monthly payments were made.
 
"""

def debt_owed(amountOwed: float, monthly_percent_payment: float, annual_percent_interest: float, payoff_as_lump_threshold: int, monthCount: int = 0):
    
    """
    amountOwed:                 The size of the loan
    monthly_percent_payment:    The percentage of the amountOwed that must be paid back each month (Typically 2%)
    annual_percent_interest:    The YEARLY percentage interest applied to the amountOwed (Typically 18%)
    payoff_as_lump_threshold:   A number in whole pounds at which point we are prepared to pay off the remaining loan in one final payment.
                                NOTE that this must be > 0 or Python reaches its maximum recursion depth.
    monthCount:                 A count of how many months it has taken to clear the loan.
    
    
    
    amountOwed is displayed to 3 decimal places to avoid confusion when amountOwed nears the lump threshold
    
    """
    
    if amountOwed <= payoff_as_lump_threshold: #when we reach a set threshold, pay off the remaining loan instead of going into pennies
        
        min_payment_value = amountOwed
               
    else:
    
        min_payment_value = amountOwed * (monthly_percent_payment / 100)
        
        
    
    balanceafterpayment = amountOwed - min_payment_value
    
    interestapplied = balanceafterpayment * ((annual_percent_interest/100) / 12)
    
    amountOwed = balanceafterpayment + interestapplied
    
    
    if amountOwed <= 0:
        
        print("Debt paid off hooray! Months taken: " + str(monthCount))
        
        message = "That's " + str(monthCount // 12) + " years"
            
        if monthCount % 12 == 0:
            print( message + "!!")
        else:
            print( message + " and " + str(monthCount % 12) + " months!!!")
        
        return True
    else:
        print("Month " + str(monthCount) + " | Paid: £" + format(min_payment_value, ',.2f') + " | Balance still to pay: £" + format(amountOwed, ',.3f') + " | Next payment due: £" + format(amountOwed * (monthly_percent_payment / 100),',.2f'))
        debt_owed(amountOwed, monthly_percent_payment, annual_percent_interest, payoff_as_lump_threshold, monthCount + 1)
    

#Run function
borrowed = 5000 #£
min_to_pay = 2  #%
annual_interest = 18 #%
payoff_threshold = 5 #£


debt_owed(borrowed, min_to_pay, annual_interest, payoff_threshold)