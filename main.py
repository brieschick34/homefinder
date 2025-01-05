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

from configurationClass import Configuration

def getTotalCosts(Configuration):
    prospectRange = 1.10

    prospectLine = Configuration.houseCost * prospectRange # Pull results where house cost no more then 1.5x listng value
    Configuration.printConfigToSTDOUT()

    if Configuration.additionalCostsOnHouse < 0:
        Configuration.writeConfigToFile("BuggyProspects")
    elif Configuration.totalCost <= prospectLine:
        Configuration.writeConfigToFile("TopProspects")
    else:
        print("NOT A PROSPECT. WILL NOT ADD TO FILE.")    
    return [ Configuration.number, Configuration.additionalCostsOnHouse ]

# Magic
def iterateOverConfigurations():
    houseCostRanges = [ 100000, 125000, 150000, 175000, 200000, 225000, 250000 ]
    downPaymentPrecentRanges = [ 0, .05, .1, .15, .2, .25, .3, .35, .4 ]
    totalConfigurations = 0
        
    f = open("VeryTopProspects.txt", "a")
    for houseCost in houseCostRanges:
        minimizedCost = 1.5 * houseCost
        for downPaymentPrecent in downPaymentPrecentRanges:
            for  i in range(1, 10):
                extraPayment = (.0005*i)*houseCost
                for i in range(1, 10):
                    totalConfigurations += 1
                    buyDownAmount = (.01*i)*houseCost
                    # if buyDownAmount <= houseCost * .1 # Only run configs for buy down amounts 
                    currentConfig = Configuration(totalConfigurations, houseCost, downPaymentPrecent, extraPayment, buyDownAmount)
                    currentCost = getTotalCosts(currentConfig)
                    if currentCost[1] <= minimizedCost:
                        minimizedCost = currentCost[1]
                        print("New Minimized Cost for House at: " + str(houseCost) + " is " + str(minimizedCost))
                    time.sleep(.5)
        f.write("Top Config for House Costing: " + str(houseCost) + " is #" + str(currentCost[0]) + " with additional costs of " + str(currentCost[1]) + "\n")
    f.close()

# START
iterateOverConfigurations()