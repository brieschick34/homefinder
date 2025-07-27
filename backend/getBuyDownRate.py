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

point_map = {
  0: 7.125,
  1: 6.875
}

def getBuyDownRate(points, interestRate):
  pts = round(points)
  ptPrecent = point_map[pts] / 100
  return ptPrecent
  # print("BuyDownRate: " + str(buydownRate))
  # print("---------------------------------------------------------------------------------")
  # return buydownRate

