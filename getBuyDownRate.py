def getBuyDownRateDrop(principal, buyDownAmount):
  getPrecentOfPrincipal = buyDownAmount / principal 
  points = getPrecentOfPrincipal / .01 
  return points * .0025

def getBuyDownRate(principal, buyDownAmount, interestRate):
  return interestRate - getBuyDownRateDrop(principal, buyDownAmount)

