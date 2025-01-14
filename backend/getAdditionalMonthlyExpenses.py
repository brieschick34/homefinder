def getHomeInsuranceMonthlyCost(principal):
    principalInK = principal / 1000
    insuranceRate = (( -0.001 * principalInK ) + 1.1 ) / 100 
    return ( [ insuranceRate, round((( insuranceRate * principal ) / 12 ), 2) ])

def getPropertyTaxMonthlyCost(principal, propertyTaxRate):
    return ( round((( propertyTaxRate * principal ) / 12 ), 2))

def getClosingCost(principal):
    principalInK = principal / 1000 
    closingCostPrecent = (( -0.0088888888888889 * principalInK ) + 6.1111111111111 ) / 100
    return ( [ closingCostPrecent,  round(principal * closingCostPrecent , 2) ])

# insuranceRate = .01
# propertyTaxRate = .0085

# principal = float(input("Enter Loan Principal:"))
# closingCostPrecent = float(input("Enter the Estimated Closing Cost as a Precent: "))

# insuranceCost = getHomeInsuranceMonthlyCost(principal, insuranceRate)
# propertyTaxCost = getPropertyTaxMonthlyCost(principal, propertyTaxRate)

# print("Insurance Cost: " + str(insuranceCost))
# print("Property Tax Cost: " + str(propertyTaxCost))
# print("Total Additional Costs: " + str(insuranceCost + propertyTaxCost))

