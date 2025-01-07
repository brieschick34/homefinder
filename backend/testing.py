from getBuyDownRate import getBuyDownRate
from getMortgageAmount import getMortgageAmount
from getPMI import getPMITotalNumOfPayments, getMonthlyPMI, getPMITotalCost
from getTermLength import getTermLength


def testGetMortgageAmount():
    houseCost = 200000
    downPaymentPrecent = .05
    monthlyRate = .0699 / 12
    termLength = 360

    principal = houseCost - ( downPaymentPrecent * houseCost ) 
    mortgageAmount = getMortgageAmount(principal, monthlyRate, termLength)

    print("Testing getMortgageAmount Function...")
    print("  -> The Mortgage Amount Per Month is: " + str(mortgageAmount))
    print("  -> Expected Mortgage Amount Per Month is: 1262.80" )


    if mortgageAmount == 1262.80:
        print("PASS!")
        print("----------------------------------------------------")
    else:
        print("FAIL")
        print("----------------------------------------------------")


def testGetTermLength():
    principal = 190000
    mortgageAmount = 1262.8
    extraPayment = 500
    interestRate = .0699 / 12

    print("Testing getTermLength Function...")
    loanTermLength = getTermLength(principal, extraPayment, mortgageAmount, interestRate)
    print("  -> Term Length for the loan is: " + str(loanTermLength))
    print("  -> Expected Length for the loan is: 171")
    
    if loanTermLength == 171:
        print("PASS!")
        print("----------------------------------------------------")
    else:
        print("FAIL")
        print("----------------------------------------------------")

def testGetBuyDownRate():
  principal = 190000
  buyDownAmount = 1900
  interestRate = .0699

  print("Testing getBuyDownRateDrop Function...")
  buyDownRate = getBuyDownRate(principal, buyDownAmount, interestRate)
  print("  -> Buy Down Rate is: " + str(buyDownRate))
  print("  -> Expected Buy Down Rate is: 6.74" )
    
  if buyDownRate == 6.74:
      print("PASS!")
      print("----------------------------------------------------")
  else:
      print("FAIL")
      print("----------------------------------------------------]")

def testPMIFunctions():
    houseCost = 200000
    downPaymentPrecent = .05
    mortgageAmount = 1262.8
    interestRate = .0699
    pmiPrecent = .0046
    extraPayment = 0
    monthlyRate = ( interestRate / 12 )

    principal = houseCost - ( downPaymentPrecent * houseCost ) 
    monthlyPMI = ( principal * pmiPrecent ) / 12

    print("Testing getPMITotalNumOfPayments Function...")
    totalPayments = getPMITotalNumOfPayments(principal, houseCost, mortgageAmount, extraPayment, monthlyRate)
    print("  -> Total PMI Payments is: " + str(totalPayments))
    print("  -> Expected Total PMI Payments is: 100" )

    if totalPayments == 100:
        print("PASS!")
        print("----------------------------------------------------")
    else:
        print("FAIL")
        print("----------------------------------------------------")

    print("Testing getMonthlyPMI Function...")
    monthlyPMI = getMonthlyPMI(principal, pmiPrecent)
    print("  -> Total Monthly PMI Payment is: " + str(monthlyPMI))
    print("  -> Expected Total Monthly PMI Payment is: 72.83")

    if monthlyPMI == 72.83:
        print("PASS!")
        print("----------------------------------------------------")
    else:
        print("FAIL")
        print("----------------------------------------------------")
        
    print("Testing getPMITotalCost Function...")
    totalPMICost = getPMITotalCost(principal, pmiPrecent, houseCost, extraPayment, mortgageAmount, monthlyRate)
    print("  -> Total PMI Cost is: " + str(totalPMICost))
    print("  -> Expected Total PMI Cost is: 6916")

    if totalPMICost == 6916:
        print("PASS!")
        print("----------------------------------------------------")
    else:
        print("FAIL")
        print("----------------------------------------------------")

def startTests():
    testGetBuyDownRate()
    testGetTermLength()
    testPMIFunctions()
    testGetTermLength()

startTests()