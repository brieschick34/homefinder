def getTermLength(principal, extraPayment, mortgageAmount, interestRate):
    termLength = 0
    while principal >= 0:
        principalPayment = ( mortgageAmount + extraPayment ) - ( principal * interestRate ) 
        principal = principal - principalPayment
        termLength += 1
        # print("Interest: " + str(principal * interestRate))
        # print("Morgage Amount + extra payment: " + str(mortgageAmount + extraPayment))
        # print("Principal Payment: " + str(principalPayment))
        # print("Principal: " + str(principal))
    return termLength    
