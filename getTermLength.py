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

def testGetTermLength():
    principal = 190000
    mortgageAmount = 1262.8
    extraPayment = 500
    interestRate = .0699

    print("Testing getMortgageAmount Function...")
    loanTermLength = getTermLength(principal, extraPayment, mortgageAmount, interestRate)
    print("  -> Term Length for the loan is: " + str(loanTermLength))
    
    if loanTermLength == 171:
        print("PASS!")
        print("----------------------------------------------------")
    else:
        print("FAIL")
        print("----------------------------------------------------")