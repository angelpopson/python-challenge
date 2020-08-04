# Angel Popa                                Date : 8/4/2020
#---------------------------------------------------------------------
## PyPoll
import os
import csv

#Path to CSV File
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("Resources/election_data.csv")

# Read the csv file
with open(csvpath) as electiondata: 
    csvreader = csv.reader(electiondata,delimiter=",")

    #Skip header
    next(electiondata)
    
    #Create variables
    totalrows = []
    Khan = []
    Li = []
    Correy = []
    OTooley = []

    #Loop through each row to find the votes that went to each candidate and add it to their count
    for row in csvreader: 
        totalrows.append(row[0])
        if row[2]=="Khan":
            Khan.append(row[2])
        elif row[2]=="Li":
            Li.append(row[2])
        elif row[2]=="Correy":
            Correy.append(row[2])
        else:
            OTooley.append(row[2])
    
    #Calculate the % of votes for each candidate 
    pctgKhan = len(Khan)/len(totalrows)
    pctgLi =  len(Li)/len(totalrows)
    pctgCorrey =  len(Correy)/len(totalrows)
    pctgOTooley =  len(OTooley)/len(totalrows)

#Find which candidate had the most votes and keep the # of votes under winner
winner = max(len(Khan),len(Li),len(Correy),len(OTooley))

#Create a dictionary listing the votes of each candidate with their name as a value
biglist = {len(Khan): "Khan", len(Li): "Li", len(Correy): "Correy", len(OTooley): "O'Tooley"}

#Loop through the dictionary and place the name of the winner on winner2
for x in biglist:
    if winner == x:
         winner2 = biglist.get(x) 

#Display calculations
output = (
f"Election Results:\n"
f"---------------------------------\n"
f"Total Votes:{len(totalrows)}\n"
f"---------------------------------\n"
f"Candidates:\n"
f"Khan: {(pctgKhan*100):.2f}% total votes: ({len(Khan)})\n"
f"Li: {(pctgLi*100):.2f}% total votes: ({len(Li)})\n"
f"Correy: {(pctgCorrey*100):.2f}% total votes: ({len(Correy)})\n"
f"O'Tooley: {(pctgOTooley*100):.2f}% total votes: ({len(OTooley)})\n"
f"---------------------------------\n"
f"And the winner is: {winner2}\n"

  
f"---------------------------------\n")
print(output)

#Create Analysis Text File
outputpath = os.path.join("Analysis", "Poll_Analysis.txt")
with open(outputpath, "w") as txt_file:
    txt_file.write(output)