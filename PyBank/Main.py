# Angel Popa                                Date : 8/4/2020
#---------------------------------------------------------------------
## PyBank
import os
import csv

#Path to CSV File
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("Resources","budget_data.csv")

#Create variables
totalmonths = 0
netprofit = 0
previousprofit = 0
monthlychange = 0
changelist = []
avgchngprofit = 0
maxinc = 0
maxdec = 0


# Read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    #skip header
    next(csvfile) 
    rowcount = []
    totalprofit = 0
    totalchange = 0
    prevvalue = 0
    totalrev = 0
    monthlyrev = []

# Loop through each after the header
    for row in csvreader: 
         #add values to list rowcount
        rowcount.append(row[1]) 
        monthlyvalue = int(row[1])
        # Calculate net amount of profit/losses
        totalprofit = totalprofit + monthlyvalue 
    for x in range(1,len(rowcount)):
        #Add to the list monthly rev the monthly change for each row
        monthlyrev.append(int(rowcount[x])-int(rowcount[x-1]))   

#Display calculations
output=(       
f"Financial Analysis\n"
f"---------------------------------\n"
f"Total Months:{(len(rowcount))}\n"
f"Total is $ {(totalprofit)}\n"
f"Average Change: ${(round(sum(monthlyrev)/(len(rowcount)-1),2))}\n"    
f"Greatest increase in Profits: ${(max(monthlyrev))}\n"      
f"Greatest Decrease in Profits: ${(min(monthlyrev))}\n")

#Create Analysis Text File
outputpath = os.path.join("Analysis", "Financial_Analysis.txt")
print(output)
with open(outputpath, "w") as txt_file:
    txt_file.write(output)