def getPMITotalNumOfPayments(principal, houseCost, mortgageAmount, extraPayment, interestRate):
    termLength = 0
    twentyPrecentMark = houseCost * .8 # 160000
    # print("Mark: " + str(twentyPrecentMark))
    while principal >= twentyPrecentMark: # 180000 >= 160000
        principalPayment = ( mortgageAmount + extraPayment ) - ( principal * interestRate)
        principal = principal - principalPayment
        termLength += 1
        # print("Interest: " + str(principal * interestRate))
        # print("Morgage Amount + extra payment: " + str(mortgageAmount + extraPayment))
        # print("Principal Payment: " + str(principalPayment))
        # print("Principal: " + str(principal))
    return termLength    

def getMonthlyPMI(principal, pmiPrecent):
    return ( round(( principal * pmiPrecent ) / 12 , 2))

def getPMITotalCost(principal, pmiPrecent, houseCost, extraPayment, mortgageAmount, interestRate):
    monthlyPMI = getMonthlyPMI(principal, pmiPrecent)
    PMITotalNumOfPayments = getPMITotalNumOfPayments(principal, houseCost, mortgageAmount, extraPayment, interestRate)
    return ( PMITotalNumOfPayments * monthlyPMI )

def testPMIFunctions():
    houseCost = 200000
    downPaymentPrecent = .05
    mortgageAmount = 1262.8
    interestRate = .0699
    pmiPrecent = .0046

    principal = houseCost - ( downPaymentPrecent * houseCost ) 
    monthlyPMI = ( principal * pmiPrecent ) / 12

    print("Testing getPMITotalNumOfPayments Function...")
    totalPayments = getPMITotalNumOfPayments(principal, houseCost, mortgageAmount, interestRate)
    print("  -> Total PMI Payments is: " + str(totalPayments))

    if totalPayments == 100:
        print("PASS!")
        print("----------------------------------------------------")
    else:
        print("FAIL")
        print("----------------------------------------------------")

    print("Testing getMonthlyPMI Function...")
    monthlyPMI = getMonthlyPMI(principal, pmiPrecent)
    print("  -> Total Monthly PMI Payment is: " + str(monthlyPMI))

    if monthlyPMI == 72.83:
        print("PASS!")
        print("----------------------------------------------------")
    else:
        print("FAIL")
        print("----------------------------------------------------")
        
    print("Testing getPMITotalCost Function...")
    totalPMICost = getPMITotalCost(principal, pmiPrecent)
    print("  -> Total PMI Cost is: " + str(totalPMICost))

    if totalPMICost == 6916:
        print("PASS!")
        print("----------------------------------------------------")
    else:
        print("FAIL")
        print("----------------------------------------------------")

# print("The Monthly PMI is:" + str(monthlyPMI))
# print("The Total Month to Pay PMI is:" + str(getPMITotalNumOfPayments(principal)))
# print("The Total Cost of the PMI is:" + str(getPMITotalCost(principal, pmiPrecent)))


