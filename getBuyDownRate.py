def getBuyDownRateDrop(principal, buyDownAmount):
  getPrecentOfPrincipal = buyDownAmount / principal 
  points = getPrecentOfPrincipal / .01 
  return points * .0025

def getBuyDownRate(principal, buyDownAmount, interestRate):
  return interestRate - getBuyDownRateDrop(principal, buyDownAmount)

def testGetBuyDownRate():
  principal = 190000
  buyDownAmount = 1900
  interestRate = .0699

  print("Testing getBuyDownRateDrop Function...")
  buyDownRate = getBuyDownRate(principal, buyDownAmount, interestRate)
  print("  -> Buy Down Rate is: " + str(buyDownRate))
    
  if buyDownRate == 6.74:
      print("PASS!")
      print("----------------------------------------------------")
  else:
      print("FAIL")
      print("----------------------------------------------------]")



