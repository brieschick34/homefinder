# def getBuyDownRateDrop(buyDownAmount):
  # rateReduceBy = .00125
  # print("---------------------------------------------------------------------------------")
  # print("BuyDownAmount: " + str(buyDownAmount))
  # print("Principal: " +  str(principal))
  # print("------------------------------------")
  # getPrecentOfPrincipal = buyDownAmount / principal 
  # print("getPrecentOfPrincipal: " + str(getPrecentOfPrincipal))
  # points = getPrecentOfPrincipal / .01 
  # print("points: " + str(points))
  # print("rateDrop: " + str(points * .0025))
  # if 

  # return points * rateReduceBy
rate_map = {}
cost_map = {}

rate_map["Gomez"] = { 
  0: 7.125,
  1: 6.875,
  2: 6.750,
  3: 6.625
}

rate_map["NEO"] = { 
  0: 7.125,
  1: 6.875,
  2: 6.625,
  3: 6.5
}

rate_map["PENFED"] = { 
  0: 7.125,
  1: 6.875,
  2: 6.625,
  3: 6.5
}

cost_map["Gomez"] = {
  0: 0,
  1: 1600,
  2: 2660,
  3: 3400
}

cost_map["NEO"] = {
  0: 0,
  1: 2125,
  2: 3984,
  3: 6109
}
cost_map["PENFED"] = {
  0: 0,
  1: 2125,
  2: 3984,
  3: 6109
}


def getBuyDownCost(points, banker_name, houseCost):
  pts = round(points)
  ptCost = cost_map[banker_name][pts] / 250000 # divide by 250k because numbs based on that
  return houseCost * ptCost

def getBuyDownRate(points, banker_name):
  pts = round(points)
  ptPrecent = rate_map[banker_name][pts] / 100
  return ptPrecent
  # print("BuyDownRate: " + str(buydownRate))
  # print("---------------------------------------------------------------------------------")
  # return buydownRate

