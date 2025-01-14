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
maxUpfrontCosts = [ 45000 ] # [  25000, 30000, 35000, 40000, 45000 ] 
prospectRanges = [ 1.0, 1.1, 1.2, 1.25, 1.3 ] 
maxMonthlyExpense = [ 2250, 2500 ]
houseCostRanges = [ 125000 ] 
downPaymentPrecentRanges = [ .2, .25, .3 ]

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
                    if Configuration.totalCost <= prospectLine:
                        if Configuration.monthlyExpense <= maxMonthly:
                            topProspectNumber += 1
                            Configuration.printConfigToSTDOUT()
                            Configuration.writeConfigToFile("TopProspects", topProspectNumber, prospectRange, maxMonthly, maxUpfrontCost)
                        else: 
                            print("Configuration does not meet Monthly Requirements.")
                            print("HOUSE %s: NOT A PROSPECT. WILL NOT ADD TO FILE." % Configuration.houseCost)    
                    else:
                        print("Configuration does not meet Total Cost Requirements.")
                        print("HOUSE %s: NOT A PROSPECT. WILL NOT ADD TO FILE." % Configuration.houseCost)    
                else: 
                    print("Configuration does not meet Up Front Cost Requirements. " + str(Configuration.upFrontCost))
                    print("HOUSE %s: NOT A PROSPECT. WILL NOT ADD TO FILE." % Configuration.houseCost)    
    return [ Configuration.number, Configuration.additionalCostsOnHouse ]

# Magic
def iterateOverConfigurations():
    totalConfigurations = 0
        
    f = open("VeryTopProspects.txt", "a")
    for houseCost in houseCostRanges:
        print("looking at house " + str(houseCost))
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