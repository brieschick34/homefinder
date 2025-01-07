# import time

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
        # time.sleep(.5)
    return termLength    

def getMonthlyPMI(principal, pmiPrecent):
    return ( round(( principal * pmiPrecent ) / 12 , 2))

def getPMITotalCost(principal, pmiPrecent, houseCost, extraPayment, mortgageAmount, monthlyRate):
    monthlyPMI = getMonthlyPMI(principal, pmiPrecent)
    PMITotalNumOfPayments = getPMITotalNumOfPayments(principal, houseCost, mortgageAmount, extraPayment, monthlyRate)
    return ( PMITotalNumOfPayments * monthlyPMI )

# print("The Monthly PMI is:" + str(monthlyPMI))
# print("The Total Month to Pay PMI is:" + str(getPMITotalNumOfPayments(principal)))
# print("The Total Cost of the PMI is:" + str(getPMITotalCost(principal, pmiPrecent)))


