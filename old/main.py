import time
from getAdditionalMonthlyExpenses import getHomeInsuranceMonthlyCost, getPropertyTaxMonthlyCost, getClosingCost
from getBuyDownRate import getBuyDownRateDrop, getBuyDownRate
from getMortgageAmount import getMortgageAmount
from getPMI import getMonthlyPMI, getPMITotalCost
from getTermLength import getTermLength

# houseCost = float(input("Enter House Cost:"))
# downPaymentPrecent = float(input("Enter Down Payment Precent:"))
# extraPayment = float(input("Enter Extra Payment Amount:"))
# buyDownAmount = float(input("Enter Buy Down Amount:"))
# interestRate = float(input("Enter Interest Rate (APY):"))
# pmiPrecent = float(input("Enter your PMI Precent: "))

totalConfigurations = 0
totalProspects = 0
prospectRange = 1.10

def getTotalCosts(houseCost, downPaymentPrecent, extraPayment, buyDownAmount, interestRate, pmiPrecent):
    insuranceRate = .01
    propertyTaxRate = .0085
    closingCostPrecent = .05
    initalTermLength = 360

    downPayment = downPaymentPrecent * houseCost 
    principal = houseCost - downPayment

    print("Down Payment: " + str(downPayment))
    print("Loan Principal: " + str(principal))

    print("Buy Down Rate: ", end="")
    buyDownRate = getBuyDownRate(principal, buyDownAmount, interestRate)
    print(str(buyDownRate))

    print("Monthly Rate with Buy Down: ", end="")
    monthlyRate = buyDownRate / 12
    print(str(monthlyRate))

    print("Monthly Mortgage Amount: ", end="")
    monthlyMortgage = getMortgageAmount(principal, monthlyRate, initalTermLength)
    print(str(monthlyMortgage))

    print("New Term Resulting From Additional Payments: ", end="")
    newTermLength = getTermLength(principal, extraPayment, monthlyMortgage, monthlyRate)
    print(str(newTermLength))

    print("Monthly PMI Cost: ", end="")
    pmiMonthlyCost = getMonthlyPMI(principal, pmiPrecent)
    print(str(pmiMonthlyCost))

    print("Total Cost of PMI till 20 Precent Equity: ", end="")
    pmiTotalCost = getPMITotalCost(principal, pmiPrecent, houseCost, monthlyMortgage, extraPayment, monthlyRate)
    print(str(pmiTotalCost))

    print("----------------------------------------------------")
    print("Totals:")
    insuranceExpense = getHomeInsuranceMonthlyCost(principal, insuranceRate) 
    propertyTaxExpense = getPropertyTaxMonthlyCost(principal, propertyTaxRate)
    closingCost = getClosingCost(principal, closingCostPrecent)

    monthlyExpenses = monthlyMortgage + pmiMonthlyCost + insuranceExpense + propertyTaxExpense
    upFrontCost = downPayment + buyDownAmount + closingCost
    totalCost = ( monthlyExpenses * newTermLength ) + upFrontCost
    additionalCostsOnHouse = totalCost - houseCost
    
    global totalConfigurations
    totalConfigurations += 1

    print("Loan Configuration #:" + str(totalConfigurations))
    print("  -> Cost of House: " + str(houseCost))
    print("  -> Down Payment Precent: " + str(downPaymentPrecent))
    print("  -> Extra Monthly Payment: " + str(extraPayment))
    print("  -> Buy Down Amount: " + str(buyDownAmount))
    print("  -> Loan Interest Rate: " + str(interestRate))
    print("  -> PMI Precent: " + str(pmiPrecent))
    print("  -> Loan Term Length (Before Extra Payments): " + str(initalTermLength))
    print("  -> Property Tax Precent: " + str(propertyTaxRate*100))
    print("  -> Closing Cost Precent: " + str(closingCostPrecent*100))
    print("  -> Home Insurance Precent: " + str(insuranceRate*100))

    print("Monthly Expenses: " + str(round(monthlyExpenses, 2)))
    print("  -> Mortgage: " + str(monthlyMortgage))
    print("  -> PMI: " + str(pmiMonthlyCost))
    print("  -> Insurance: " + str(insuranceExpense))
    print("  -> Property Tax: " + str(propertyTaxExpense))

    print("Up Front Costs: " + str(round(upFrontCost, 2)))
    print("  -> Down Payment: " + str(downPayment))
    print("  -> Buy Down Amount: " + str(buyDownAmount))
    print("  -> Estimated Additional Closing Costs ( " + str(closingCostPrecent*100) + "% ): "  + str(closingCost))

    print("Total Cost: " + str(round(totalCost,2)))
    print("Amount Paid on Top of House Cost: " + str(additionalCostsOnHouse))
    print("Amount Paid on Top of House Cost (Precent): " + str((additionalCostsOnHouse/totalCost)*100))

    prospectLine = houseCost * prospectRange # Pull results where house cost no more then 1.5x listng value
    if additionalCostsOnHouse < 0:
        f = open("BuggyProspects.txt", "a")
        f.write("Loan Configuration #:" + str(totalConfigurations) + "\n")
        f.write("  -> Cost of House: " + str(houseCost) + "\n")
        f.write("  -> Down Payment Precent: " + str(downPaymentPrecent) + "\n")
        f.write("  -> Extra Monthly Payment: " + str(extraPayment) + "\n")
        f.write("  -> Buy Down Amount: " + str(buyDownAmount) + "\n")
        f.write("  -> Loan Interest Rate: " + str(interestRate) + "\n")
        f.write("  -> PMI Precent: " + str(pmiPrecent) + "\n")
        f.write("  -> Loan Term Length (Before Extra Payments): " + str(initalTermLength) + "\n")
        f.write("  -> Property Tax Precent: " + str(propertyTaxRate*100) + "\n")
        f.write("  -> Closing Cost Precent: " + str(closingCostPrecent*100) + "\n")
        f.write("  -> Home Insurance Precent: " + str(insuranceRate*100) + "\n")
        
        f.write("Calculated Numbers: " + "\n")
        f.write("  -> Down Payment:: " + str(downPayment) + "\n")
        f.write("  -> Loan Principal: " + str(principal) + "\n")
        f.write("  -> Buy Down Rate: " + str(buyDownRate) + "\n")
        f.write("  -> New Term Length: " + str(newTermLength) + "\n")
        f.write("  -> Total Cost of PMI till 20 Precent Equity: " + str(pmiTotalCost) + "\n")

        f.write("Monthly Expenses: " + str(round(monthlyExpenses, 2)) + "\n")
        f.write("  -> Mortgage: " + str(monthlyMortgage) + "\n")
        f.write("  -> PMI: " + str(pmiMonthlyCost) + "\n")
        f.write("  -> Insurance: " + str(insuranceExpense) + "\n")
        f.write("  -> Property Tax: " + str(propertyTaxExpense) + "\n")

        f.write("Up Front Costs: " + str(round(upFrontCost, 2)) + "\n")
        f.write("  -> Down Payment: " + str(downPayment) + "\n")
        f.write("  -> Buy Down Amount: " + str(buyDownAmount) + "\n")
        f.write("  -> Estimated Additional Closing Costs ( " + str(closingCostPrecent*100) + "% ): "  + str(closingCost) + "\n")

        f.write("Total Cost: " + str(round(totalCost,2)) + "\n")
        f.write("Amount Paid on Top of House Cost: " + str(additionalCostsOnHouse) + "\n")
        f.write("Amount Paid on Top of House Cost (Precent): " + str((additionalCostsOnHouse/totalCost)*100) + "\n")

        f.write("--------------------------------------------------------------------------------------------------------\n")
        f.close()
    elif totalCost <= prospectLine:
        global totalProspects
        totalProspects += 1

        f = open("TopProspects.txt", "a")
        f.write("Loan Configuration #:" + str(totalConfigurations) + "\n")
        f.write("Prospect Configuration #:" + str(totalProspects) + "\n")
        f.write("  -> Cost of House: " + str(houseCost) + "\n")
        f.write("  -> Down Payment Precent: " + str(downPaymentPrecent) + "\n")
        f.write("  -> Extra Monthly Payment: " + str(extraPayment) + "\n")
        f.write("  -> Buy Down Amount: " + str(buyDownAmount) + "\n")
        f.write("  -> Loan Interest Rate: " + str(interestRate) + "\n")
        f.write("  -> PMI Precent: " + str(pmiPrecent) + "\n")
        f.write("  -> Loan Term Length (Before Extra Payments): " + str(initalTermLength) + "\n")
        f.write("  -> Property Tax Precent: " + str(propertyTaxRate*100) + "\n")
        f.write("  -> Closing Cost Precent: " + str(closingCostPrecent*100) + "\n")
        f.write("  -> Home Insurance Precent: " + str(insuranceRate*100) + "\n")

        f.write("Calculated Numbers: " + "\n")
        f.write("  -> Down Payment:: " + str(downPayment) + "\n")
        f.write("  -> Loan Principal: " + str(principal) + "\n")
        f.write("  -> Buy Down Rate: " + str(buyDownRate) + "\n")
        f.write("  -> New Term Length: " + str(newTermLength) + "\n")
        f.write("  -> Total Cost of PMI till 20 Precent Equity: " + str(pmiTotalCost) + "\n")

        f.write("Monthly Expenses: " + str(round(monthlyExpenses, 2)) + "\n")
        f.write("  -> Mortgage: " + str(monthlyMortgage) + "\n")
        f.write("  -> PMI: " + str(pmiMonthlyCost) + "\n")
        f.write("  -> Insurance: " + str(insuranceExpense) + "\n")
        f.write("  -> Property Tax: " + str(propertyTaxExpense) + "\n")

        f.write("Up Front Costs: " + str(round(upFrontCost, 2)) + "\n")
        f.write("  -> Down Payment: " + str(downPayment) + "\n")
        f.write("  -> Buy Down Amount: " + str(buyDownAmount) + "\n")
        f.write("  -> Estimated Additional Closing Costs ( " + str(closingCostPrecent*100) + "% ): "  + str(closingCost) + "\n")

        f.write("Total Cost: " + str(round(totalCost,2)) + "\n")
        f.write("Amount Paid on Top of House Cost: " + str(additionalCostsOnHouse) + "\n")
        f.write("Amount Paid on Top of House Cost (Precent): " + str((additionalCostsOnHouse/totalCost)*100) + "\n")

        f.write("--------------------------------------------------------------------------------------------------------\n")
        f.close()
    else:
        print("NOT A PROSPECT. WILL NOT ADD TO FILE.")    

    print("----------------------------------------------------")
    print("----------------------------------------------------")     
    return [ totalConfigurations, additionalCostsOnHouse ]

# Magic
interestRate =.0699
pmiPrecent = .0046

houseCostRanges = [ 100000, 125000, 150000, 175000, 200000, 225000, 250000 ]
downPaymentPrecentRanges = [ 0, .05, .1, .15, .2, .25, .3, .35, .4 ]
    
f = open("VeryTopProspects.txt", "a")
for houseCost in houseCostRanges:
    minimizedCost = 1.5 * houseCost
    for downPaymentPrecent in downPaymentPrecentRanges:
        for  i in range(1, 10):
            extraPayment = (.0005*i)*houseCost
            for i in range(1, 10):
                buyDownAmount = (.1*i)*houseCost
                currentCost = getTotalCosts(houseCost, downPaymentPrecent, extraPayment, buyDownAmount, interestRate, pmiPrecent)
                if currentCost[1] <= minimizedCost:
                    minimizedCost = currentCost[1]
                    print("New Minimized Cost for House at: " + str(houseCost) + " is " + str(minimizedCost))
                time.sleep(.5)
    f.write("Top Config for House Costing: " + str(houseCost) + " is #" + str(currentCost[0]) + " with additional costs of " + str(currentCost[1]) + "\n")
f.close()
