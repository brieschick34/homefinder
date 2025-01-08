# import time
from pathlib import Path

def getTermLength(principal, extraPayment, mortgageAmount, interestRate, generateReport):
    termLength = 0
    totalInterest = 0
    payment = mortgageAmount + extraPayment 

    
    initalRow = ["0", "0", "0", "0", principal]
    rows = [initalRow]

    if generateReport:
        fileNameArr = (str(principal), str(extraPayment), str(mortgageAmount), str(round(interestRate, 4)))
        fileName = "-".join(fileNameArr)
        print("Writing Amortization Report: " + fileName)
        folderName = "reports/amortizationSchedules/"
        Path(folderName).mkdir(parents=True, exist_ok=True)
        f = open("%s/%s.txt" % ( folderName, fileName ), "a")
        f.write("Amortization Schedule For " + str(principal) + " dollar loan.\n")
        f.write("Morgage Amount of " + str(mortgageAmount) + " at a rate of " + str(interestRate) + "\n")
        f.write("Extra Payments of " + str(extraPayment) + "\n")
        f.write("---------------------------------------------------------------------------\n")
    
    while principal >= 0:
        interest = principal * interestRate 
        totalInterest = totalInterest + interest
        principalPayment =  payment - interest
        principal = principal - principalPayment
        termLength += 1
        
        newRow = [ termLength, payment, interest, principalPayment, principal ]
        rows.append(newRow)

        if generateReport: 
            f.write("Payment: #" + str(termLength) + " | Payment: $" + str(payment) + " | Interest: $" + str(interest) + " | Principal Paid:  $" + str(principalPayment) + " || Remaining Balance: $" + str(principal) + "\n")
        # print("---------------------------------------------------------------------------")
        # print("Interest: " + str(principal * interestRate))
        # print("Morgage Amount + extra payment: " + str(mortgageAmount + extraPayment))
        # print("Principal Payment: " + str(principalPayment))
        # print("Principal: " + str(principal))
        # print("---------------------------------------------------------------------------")
        # time.sleep(.25)
    if generateReport:   
        f.close()   
    return [ termLength, totalInterest, rows ]    

# print("TERM LENGTH: " + str(getTermLength(85000, 450, 728.7, (.0499/12))))