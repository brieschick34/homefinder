def intermediateCalculation(monthlyRate, termLength):
    return (( 1 + monthlyRate ) ** termLength)

def getMortgageAmount(principal, monthlyRate, termLength):
    i = intermediateCalculation(monthlyRate, termLength)
    mortgageAmount = round((principal * ((monthlyRate * i)/(i - 1))), 2)
    return mortgageAmount

def testGetMortgageAmount():
    houseCost = 200000
    downPaymentPrecent = .05
    monthlyRate = .0699 / 12
    termLength = 360

    principal = houseCost - ( downPaymentPrecent * houseCost ) 
    mortgageAmount = getMortgageAmount(principal, monthlyRate, termLength)

    print("Testing getMortgageAmount Function...")
    print("  -> The Mortgage Amount Per Month is: " + str(mortgageAmount))

    if mortgageAmount == 1262.80:
        print("PASS!")
        print("----------------------------------------------------")
    else:
        print("FAIL")
        print("----------------------------------------------------")