# rebuildCost = lower house < 170k, 1% @350k .75
# insuranceRate =  # .01
# closingCostPrecent =# @350k 3%, 150k 5% 7500 - 12k .05

propertyTaxRate = .0119 # .0085
initalTermLength = 360
interestRate =.0699
pmiPrecent = .0025 #.0046
generateReports = False

from pathlib import Path
from getAdditionalMonthlyExpenses import getHomeInsuranceMonthlyCost, getPropertyTaxMonthlyCost, getClosingCost
from getBuyDownRate import getBuyDownRateDrop, getBuyDownRate
from getMortgageAmount import getMortgageAmount
from getTermLength import getTermLength
from getPMI import getMonthlyPMI, getPMITotalCost

class Configuration:
  def __init__(self, number, houseCost, downPaymentPrecent, extraPayment, buyDownAmount):
    self.number = number
    # self.uniqueNumber = uniqueNumber
    self.houseCost = houseCost
    self.downPaymentPrecent = downPaymentPrecent
    self.downPayment = downPaymentPrecent * houseCost 
    self.principal = houseCost - self.downPayment
    self.extraPayment = extraPayment
    self.buyDownAmount = buyDownAmount
    self.buyDownRate = getBuyDownRate(self.principal, buyDownAmount, interestRate)
    self.monthlyRate = self.buyDownRate / 12
    self.monthlyMortgage = getMortgageAmount(self.principal, self.monthlyRate, initalTermLength)
    self.termLengthResults =  getTermLength(self.principal, extraPayment, self.monthlyMortgage, self.monthlyRate, generateReports)
    self.newTermLength = self.termLengthResults[0]
    self.totalInterest = self.termLengthResults[1]
    self.pmiTotalCost = getPMITotalCost(self.principal, pmiPrecent, houseCost, self.monthlyMortgage, extraPayment, self.monthlyRate)
    self.pmiMonthlyCost = getMonthlyPMI(self.principal, pmiPrecent) 
    self.insuranceExpense = getHomeInsuranceMonthlyCost(self.principal) 
    self.propertyTaxExpense = getPropertyTaxMonthlyCost(self.principal, propertyTaxRate)
    self.closingCosts = getClosingCost(self.principal)
    self.monthlyExpense = self.monthlyMortgage + self.pmiMonthlyCost + self.insuranceExpense[1] + self.propertyTaxExpense + extraPayment
    self.upFrontCost = self.downPayment + self.buyDownAmount + self.closingCosts[1]
    self.totalCost = self.principal + self.totalInterest  + self.upFrontCost
    self.additionalCostsOnHouse = self.totalCost - houseCost
    self.additionalCostsOnHousePercent = ((self.totalCost / self.houseCost ) - 1 )* 100 

  def printConfigToSTDOUT(self):
    print("Loan Configuration #:" + str(self.number))
    print("  -> Cost of House: " + str(self.houseCost))
    print("  -> Down Payment Precent: " + str(self.downPaymentPrecent*100))
    print("  -> Extra Monthly Payment: " + str(self.extraPayment))
    print("  -> Buy Down Amount: " + str(self.buyDownAmount))
    print("  -> Loan Interest Rate: " + str(interestRate*100))
    print("  -> PMI Precent: " + str(pmiPrecent*100))
    print("  -> Loan Term Length (Before Extra Payments): " + str(initalTermLength))
    print("  -> Property Tax Precent: " + str(propertyTaxRate*100))
    print("  -> Closing Cost Precent: " + str(self.closingCosts[0]*100))
    print("  -> Home Insurance Precent: " + str(self.insuranceExpense[0]*100))

    print("Calculated Numbers: ")
    print("  -> Down Payment:: " + str(self.downPayment))
    print("  -> Loan Principal: " + str(self.principal))
    print("  -> Buy Down Rate: " + str(self.buyDownRate*100))
    print("  -> New Term Length: " + str(self.newTermLength))
    print("  -> Total Cost of PMI till 20 Precent Equity: " + str(self.pmiTotalCost))

    print("Monthly Expenses: " + str(round(self.monthlyExpense, 2)))
    print("  -> Mortgage: " + str(self.monthlyMortgage))
    print("  -> PMI: " + str(self.pmiMonthlyCost))
    print("  -> Insurance: " + str(self.insuranceExpense))
    print("  -> Property Tax: " + str(self.propertyTaxExpense))
    print("  -> Extra Payment: " + str(self.extraPayment))

    print("Up Front Costs: " + str(round(self.upFrontCost, 2)))
    print("  -> Down Payment: " + str(self.downPayment))
    print("  -> Buy Down Amount: " + str(self.buyDownAmount))
    print("  -> Estimated Additional Closing Costs ( " + str(self.closingCosts[0]*100) + "% ): "  + str(self.closingCosts[1]))

    print("Total Cost: " + str(round(self.totalCost,2)))
    print("Amount Paid on Top of House Cost: " + str(self.additionalCostsOnHouse))
    print("Amount Paid on Top of House Cost (Precent): " + str(self.additionalCostsOnHousePercent))

  def writeConfigToFile(self, filename, uniqueNumber, prospectRange, maxMonthlyExpense, maxUpfrontCost):
    path = "reports/automated/%sKHouse/%sKMaxClosingCost/%sMaxMonthlyCost/" % ( int(self.houseCost/1000), int(maxUpfrontCost/1000), int(maxMonthlyExpense))
    Path(path).mkdir(parents=True, exist_ok=True)
    f = open("%s/%sOfTotalCost.txt" % ( path, prospectRange) , "a")
    f.write("Loan Configuration #:" + str(self.number) + "\n")
    f.write("%s Configuration #:" % filename + str(uniqueNumber) + "\n")
    f.write("  -> Cost of House: " + str(self.houseCost) + "\n")
    f.write("  -> Down Payment Precent: " + str(self.downPaymentPrecent*100) + "\n")
    f.write("  -> Extra Monthly Payment: " + str(self.extraPayment) + "\n")
    f.write("  -> Buy Down Amount: " + str(self.buyDownAmount) + "\n")
    f.write("  -> Loan Interest Rate: " + str(interestRate*100) + "\n")
    f.write("  -> PMI Precent: " + str(pmiPrecent*100) + "\n")
    f.write("  -> Loan Term Length (Before Extra Payments): " + str(initalTermLength) + "\n")
    f.write("  -> Property Tax Precent: " + str(propertyTaxRate*100) + "\n")
    f.write("  -> Closing Cost Precent: " + str(self.closingCosts[0]*100) + "\n")
    f.write("  -> Home Insurance Precent: " + str( self.insuranceExpense[0]*100) + "\n")

    f.write("Calculated Numbers: " + "\n")
    f.write("  -> Down Payment:: " + str(self.downPayment) + "\n")
    f.write("  -> Loan Principal: " + str(self.principal) + "\n")
    f.write("  -> Buy Down Rate: " + str(self.buyDownRate*100) + "\n")
    f.write("  -> New Term Length: " + str(self.newTermLength) + "\n")
    f.write("  -> Total Cost of PMI till 20 Precent Equity: " + str(self.pmiTotalCost) + "\n")

    f.write("Monthly Expenses: " + str(round(self.monthlyExpense, 2)) + "\n")
    f.write("  -> Mortgage: " + str(self.monthlyMortgage) + "\n")
    f.write("  -> PMI: " + str(self.pmiMonthlyCost) + "\n")
    f.write("  -> Insurance: " + str(self.insuranceExpense[1]) + "\n")
    f.write("  -> Property Tax: " + str(self.propertyTaxExpense) + "\n")
    f.write("  -> Extra Payment: " + str(self.extraPayment) + "\n")

    f.write("Up Front Costs: " + str(round(self.upFrontCost, 2)) + "\n")
    f.write("  -> Down Payment: " + str(self.downPayment) + "\n")
    f.write("  -> Buy Down Amount: " + str(self.buyDownAmount) + "\n")
    f.write("  -> Estimated Additional Closing Costs ( " + str(self.closingCosts[0]*100) + "% ): "  + str(self.closingCosts[1]) + "\n")

    f.write("Total Cost: " + str(round(self.totalCost,2)) + "\n")
    f.write("Amount Paid on Top of House Cost: " + str(self.additionalCostsOnHouse) + "\n")
    f.write("Amount Paid on Top of House Cost (Precent): " + str(self.additionalCostsOnHousePercent) + "\n")

    f.write("--------------------------------------------------------------------------------------------------------\n")
    f.close()

