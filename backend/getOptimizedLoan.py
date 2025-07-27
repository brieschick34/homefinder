from configurationClass import Configuration

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
downPaymentInterval = 1000

def iterateOverConfigurations(minUpFrontCost, maxUpFrontCost, minimumHouseCost, maximumHouseCost, minMonthlyCost, maxMonthlyCost, minDownPaymentCost, maxDownPaymentCost):
    upFrontCosts = list(range(minUpFrontCost, maxUpFrontCost + 1, upFrontCostInterval))
    HouseCosts = list(range(minimumHouseCost, maximumHouseCost + 1, houseCostInterval))
    monthlyCosts = list(range(minMonthlyCost, maxMonthlyCost + 1, monthlyCostInterval))
    downPayments = list(range(minDownPaymentCost, maxDownPaymentCost + 1, downPaymentInterval))
    results = {}

    for houseCost in HouseCosts:
        minimizedCost = 3 * houseCost
        print("looking at house " + str(houseCost))
        for downPayment in downPayments:
            for buyDownRate in range(0, 1):
                for monthlyCost in monthlyCosts:
                    buyDownAmount = (.01*buyDownRate)*houseCost
                    currentConfig = Configuration(houseCost, downPayment/houseCost, buyDownAmount, monthlyCost)
                    if currentConfig.additionalCostsOnHouse <= minimizedCost:
                        # print("New house found with extra cost of: " + str(currentConfig.additionalCostsOnHouse))
                        # currentConfig.printConfigToSTDOUT()
                        minimizedCost = currentConfig.additionalCostsOnHouse
                        results[houseCost] = currentConfig

    for houseCost in HouseCosts:
        print("--------------------" + "COST OF HOUSE: " + str(houseCost) + "--------------------")
        results[houseCost].printConfigToSTDOUT()

iterateOverConfigurations(40000, 50000, 200000, 260000,1500,2500,20000,50000)