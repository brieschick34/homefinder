def intermediateCalculation(monthlyRate, termLength):
    return (( 1 + monthlyRate ) ** termLength)

def getMortgageAmount(principal, monthlyRate, termLength):
    i = intermediateCalculation(monthlyRate, termLength)
    mortgageAmount = round((principal * ((monthlyRate * i)/(i - 1))), 2)
    return mortgageAmount