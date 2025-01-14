def getBuyDownRateDrop(principal, buyDownAmount):
  rateReduceBy = .00125
  # print("---------------------------------------------------------------------------------")
  # print("BuyDownAmount: " + str(buyDownAmount))
  # print("Principal: " +  str(principal))
  # print("------------------------------------")
  getPrecentOfPrincipal = buyDownAmount / principal 
  # print("getPrecentOfPrincipal: " + str(getPrecentOfPrincipal))
  points = getPrecentOfPrincipal / .01 
  # print("points: " + str(points))
  # print("rateDrop: " + str(points * .0025))
  return points * rateReduceBy

def getBuyDownRate(principal, buyDownAmount, interestRate):
  buydownRate = interestRate - getBuyDownRateDrop(principal, buyDownAmount)
  # print("BuyDownRate: " + str(buydownRate))
  # print("---------------------------------------------------------------------------------")
  return buydownRate

