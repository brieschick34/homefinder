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
maxUpfrontCosts = [ 40000, 4250, 45000, 47500, 50000 ] # [  25000, 30000, 35000, 40000, 45000 ] 
prospectRanges = [ 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6 ] 
maxMonthlyExpense = [ 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500 ]
houseCostRanges = [ 240000, 245000, 250000, 255000, 260000, 265000, 270000  ] 
downPaymentPrecentRanges = [ .1, .125, .15, .175, .2, .225, .25, .275, .3 ]

def getTotalCosts(Configuration):
    global topProspectNumber
    global buggyProspectNumber

    for prospectRange in prospectRanges:
        for maxUpfrontCost in maxUpfrontCosts:   
            prospectLine = Configuration.houseCost * prospectRange # Pull results where house cost no more then 1.5x listng value
            Configuration.printConfigToSTDOUT()
            if Configuration.additionalCostsOnHouse < 0:
                buggyProspectNumber += 1
                Configuration.writeConfigToFile("BuggyProspects", buggyProspectNumber)
            elif Configuration.upFrontCost <= maxUpfrontCost:
                if Configuration.totalCost <= prospectLine:
                    if Configuration.monthlyExpense <= Configuration.maxMonthly:
                        topProspectNumber += 1
                        Configuration.printConfigToSTDOUT()
                        Configuration.writeConfigToFile("TopProspects", topProspectNumber, prospectRange, maxUpfrontCost)
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
            for maxMonthly in maxMonthlyExpense:
            # for  i in range(1, 10):
                # extraPayment = (.0005*i)*houseCost
                for i in range(0, 10):
                    totalConfigurations += 1
                    buyDownAmount = (.01*i)*houseCost
                    print("Craeting config")
                    currentConfig = Configuration(totalConfigurations, houseCost, downPaymentPrecent, maxMonthly, buyDownAmount)
                    print("Config Created")
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