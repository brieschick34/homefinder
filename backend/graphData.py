import matplotlib.pyplot as plt 
import pandas as pd
from pathlib import Path
import csv 
from configurationClass import Configuration

def createCSVFile(houseCost):
    csvFolderPath = "reports/automated/csv"
    csvFilePath = "%s/graph%sKData.csv" % (csvFolderPath,  int(houseCost/1000))
    Path(csvFolderPath).mkdir(parents=True, exist_ok=True)
    f = open(csvFilePath , "a")
    f.write("Total Cost,Up Front Cost\n")
    f.close()

def createRowInCSV(Configuration):
    csvFilePath = "reports/automated/csv/graph%sKData.csv" % int(Configuration.houseCost/1000)
    f = open(csvFilePath , "a")
    # dataArr = [str(Configuration.totalCost),str(Configuration.downPaymentPrecent), str(Configuration.extraPayment), str(Configuration.buyDownAmount)]
    dataArr = [str(Configuration.totalCost), str(Configuration.upFrontCost)]
    row = ",".join(dataArr)
    f.write(row + "\n")
    f.close()

def createGraphFromCSV(houseCost):
    csvFilePath = "reports/automated/csv/graph%sKData.csv" % int(houseCost/1000)
    # remove_duplicates(csvFilePath)

    # Read the CSV file
    data = pd.read_csv(csvFilePath)
    print(data.columns.tolist()) 

    # Assuming your CSV has columns like "x", "y1", "y2", etc.
    y_column = "Total Cost"
    x_column = "Up Front Cost"  # Add more columns as needed

    # Create the plot
    plt.figure()
    plt.plot(data[x_column], data[y_column], label=x_column)

    plt.xlabel("Loan Variables")
    plt.ylabel("Total House Cost")
    plt.title("Change of $%s House Cost" % houseCost)
    plt.legend()
    plt.grid(True)
    plt.show()

# def createGraphFromCSV(houseCost):
#     csvFilePath = "reports/automated/csv/graph%sKData.csv" % int(houseCost/1000)
#     remove_duplicates(csvFilePath)
#     for i in range(0,3):
#         x = [] 
#         y = [] 
#         with open(csvFilePath,'r') as csvfile: 
#             lines = csv.reader(csvFilePath, delimiter=',') 
#             for row in lines: 
#                 x.append(float(row[i]))
#                 y.append(int(row[4])) 
        
#             plt.plot(x, y, color = 'g', linestyle = 'dashed', 
#                     marker = 'o',label = "%sK House Data" % int(houseCost/1000)) 
#             plt.xticks(rotation = 25) 
#             plt.xlabel('Input') 
#             plt.ylabel('Total House Cost') 
#             plt.title("%sK House Data" % int(houseCost/1000), fontsize = 20) 
#             plt.grid() 
#             plt.legend() 
#             plt.show() 