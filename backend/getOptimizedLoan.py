from configurationClass import Configuration
from collections import defaultdict

# upFrontCostInterval = int - Defined by Dev
# Minimum Up front costs - int - inp
# Maximum Up Front costs - int - inp

# monthlyCostInterval - int - defined by Dev
# Minimum Monthly Cost - int - inp
# Maximum Monthly Cost - int - inp

# houseCostInterval - int - defined by dev
# minimumHouseCost - int - defined by dev
# maximumHouseCost - int - defined by dev

# downPaymentInterval - int - defined by dev
# minimumDownaPaymentCost - int - defined by dev
# maximumDownaPaymentCost - int - defined by dev

upFrontCostInterval = 1000
houseCostInterval = 5000
monthlyCostInterval = 100
bankers = ["Gomez", "NEO"]

def iterateOverConfigurations(minUpFrontCost, maxUpFrontCost, minimumHouseCost, maximumHouseCost, minMonthlyCost, maxMonthlyCost):
    upFrontCosts = list(range(minUpFrontCost, maxUpFrontCost + 1, upFrontCostInterval))
    HouseCosts = list(range(minimumHouseCost, maximumHouseCost + 1, houseCostInterval))
    monthlyCosts = list(range(minMonthlyCost, maxMonthlyCost + 1, monthlyCostInterval))

    results = defaultdict(lambda: defaultdict(dict))
    stdOUT = defaultdict(lambda: defaultdict(dict))

    for houseCost in HouseCosts:
        print("looking at house " + str(houseCost))
        for upFrontCost in upFrontCosts:
            for monthlyCost in monthlyCosts:
                minimizedCost = 10 * houseCost # set really high so next one gets set.
                minObj = None
                for buyDownPts in range(0, 4):
                    for banker in bankers:
                        # buyDownAmount = (.01*buyDownRate)*houseCost
                        currentConfig = Configuration(houseCost, upFrontCost, buyDownPts, monthlyCost, banker)
                        stdOUT[houseCost][upFrontCost][monthlyCost] = currentConfig

                        if currentConfig.additionalCostsOnHouse <= minimizedCost and currentConfig.monthlyExpense <= monthlyCost:
                            # print("New house found with extra cost of: " + str(currentConfig.additionalCostsOnHouse))
                            # currentConfig.printConfigToSTDOUT()
                            minimizedCost = currentConfig.additionalCostsOnHouse
                            minObj = currentConfig
                if minObj != None:            
                    results[houseCost][upFrontCost][monthlyCost] = minObj.createResponseObject()
                # print("Best house with extra cost: " + str(minObj.additionalCostsOnHouse))
                # print("Banker is: " + str(minObj.banker_name))
                # print("Buy Down Pts: " + str(minObj.buyDownPts))
                # minObj.printConfigToSTDOUT()

    # for houseCost in HouseCosts:
    #     for upFrontCost in upFrontCosts:
    #         for monthlyCost in monthlyCosts:
    #             print("--------------------" + "COST OF HOUSE: " + str(houseCost) + "--------------------")
    #             stdOUT[houseCost][upFrontCost][monthlyCost].printConfigToSTDOUT()

    return results

# iterateOverConfigurations(40000, 50000, 240000, 270000,1500,2500)