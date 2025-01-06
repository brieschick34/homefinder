import time
# from getAdditionalMonthlyExpenses import getHomeInsuranceMonthlyCost, getPropertyTaxMonthlyCost, getClosingCost
# from getBuyDownRate import getBuyDownRateDrop, getBuyDownRate
# from getMortgageAmount import getMortgageAmount
# from getPMI import getMonthlyPMI, getPMITotalCost
# from getTermLength import getTermLength
from configurationClass import Configuration
from graphData import createRowInCSV, createGraphFromCSV, createCSVFile
# houseCost = float(input("Enter House Cost:"))
# downPaymentPrecent = float(input("Enter Down Payment Precent:"))
# extraPayment = float(input("Enter Extra Payment Amount:"))
# buyDownAmount = float(input("Enter Buy Down Amount:"))
# interestRate = float(input("Enter Interest Rate (APY):"))
# pmiPrecent = float(input("Enter your PMI Precent: "))


topProspectNumber = 0
buggyProspectNumber = 0
maxUpfrontCosts = [ 30000, 35000, 40000, 45000, 50000 ]
prospectRanges = [ 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75 ]
maxMonthlyExpense = [ 2000, 2250, 2500, 2750 ]
houseCostRanges = [ 180000, 200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000 ]
downPaymentPrecentRanges = [ 0, .05, .1, .15, .2, .25, .3, .35 ]

def getTotalCosts(Configuration):
    global topProspectNumber
    global buggyProspectNumber

    for maxMonthly in maxMonthlyExpense:
        for prospectRange in prospectRanges:
            for maxUpfrontCost in maxUpfrontCosts:   
                prospectLine = Configuration.houseCost * prospectRange # Pull results where house cost no more then 1.5x listng value
                if Configuration.additionalCostsOnHouse < 0:
                    buggyProspectNumber += 1
                    Configuration.writeConfigToFile("BuggyProspects", buggyProspectNumber)
                elif Configuration.upFrontCost <= maxUpfrontCost:
                    print("Configuration does not meet Up Front Cost Requirements.")
                    if Configuration.totalCost <= prospectLine:
                        print("Configuration does not meet Total Cost Requirements.")
                        if Configuration.monthlyExpense <= maxMonthly:
                            print("Configuration does not meet Monthly Requirements.")
                            topProspectNumber += 1
                            Configuration.printConfigToSTDOUT()
                            Configuration.writeConfigToFile("TopProspects", topProspectNumber, prospectRange, maxMonthly, maxUpfrontCost)
    else:
        print("NOT A PROSPECT. WILL NOT ADD TO FILE.")    
    return [ Configuration.number, Configuration.additionalCostsOnHouse ]

# Magic
def iterateOverConfigurations():
    totalConfigurations = 0
        
    f = open("VeryTopProspects.txt", "a")
    for houseCost in houseCostRanges:
        minimizedCost = 1.5 * houseCost
        createCSVFile(houseCost)
        for downPaymentPrecent in downPaymentPrecentRanges:
            for  i in range(1, 10):
                extraPayment = (.0005*i)*houseCost
                for i in range(1, 10):
                    totalConfigurations += 1
                    buyDownAmount = (.01*i)*houseCost
                    currentConfig = Configuration(totalConfigurations, houseCost, downPaymentPrecent, extraPayment, buyDownAmount)
                    createRowInCSV(currentConfig)
                    currentCost = getTotalCosts(currentConfig)
                    if currentCost[1] <= minimizedCost:
                        minimizedCost = currentCost[1]
                        # print("New Minimized Cost for House at: " + str(houseCost) + " is " + str(minimizedCost))
                        # time.sleep(.5)
        f.write("Top Config for House Costing: " + str(houseCost) + " is #" + str(currentCost[0]) + " with additional costs of " + str(currentCost[1]) + "\n")
    f.close()

def graphConfigurations():
    for hostCost in houseCostRanges:
        createGraphFromCSV(hostCost)
        time.sleep(2.5)

# START
iterateOverConfigurations()
# graphConfigurations()