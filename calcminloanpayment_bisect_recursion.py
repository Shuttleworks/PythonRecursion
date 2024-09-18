# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:22:59 2024

@author: Shuttleworks

Find the minimum fixed payment possible to pay off a loan incurring compound interest in 12 months.
Accuracy to the nearest penny. 
Implements bisection search and recursion.
"""

def FindMinFixedPayment(balance, annualInterestRate):
    
    monthlyInterestRate = annualInterestRate / 12.0

    monthlyPaymentLbound = balance / 12
    
    #print("Monthly payment lBound " + str(monthlyPaymentLbound))

    compoundedInterest = (1 + monthlyInterestRate) ** 12

    monthlyPaymentUbound = (balance * compoundedInterest)/12.0
    
    #print("Monthly payment uBound " + str(monthlyPaymentUbound))
    
    def GetMidPointValue(lBound, uBound):
        return (lBound + uBound) / 2

    def TestPayment(balance, monthlyPaymentLbound, monthlyPaymentUbound):

        balanceRemaining = balance
        payment = GetMidPointValue(monthlyPaymentLbound, monthlyPaymentUbound)
        #print("Payment : " + str(payment))
        
        if format(monthlyPaymentLbound,".2f") >= format(monthlyPaymentUbound, ".2f"):
        
            print("Lowest Payment: £" + format(monthlyPaymentLbound, ".2f") + " (Ubound sanity check: £" + format(monthlyPaymentUbound,".2f") + ")")
            return True;
        
        
        for x in range(0, 12):
            
            balanceRemaining  = balanceRemaining - payment
            interestApplied = balanceRemaining * (annualInterestRate / 12)
            balanceRemaining = balanceRemaining + interestApplied
            
       
        if balanceRemaining < 0.01:
            #we paid too much per month, make the mid point the new upperbound
            print("Old payment: " + str(payment) + " Overpaid by : " + str(balanceRemaining))
            monthlyPaymentUbound = payment
           
            return TestPayment(balance,  monthlyPaymentLbound, monthlyPaymentUbound)
        
        elif balanceRemaining > 0.01:
            #we didn't pay enough per month, make the mid point the new lowerbound
            print("Old payment: " + str(payment) + " Underpaid - Balance Still Remaining: " + str(balanceRemaining))
            
            monthlyPaymentLbound = payment
                      
            return TestPayment(balance,  monthlyPaymentLbound, monthlyPaymentUbound)
        
        

    return TestPayment(balance, monthlyPaymentLbound, monthlyPaymentUbound)


balance = 999999

annualInterestRate = 0.18

FindMinFixedPayment(balance, annualInterestRate)
