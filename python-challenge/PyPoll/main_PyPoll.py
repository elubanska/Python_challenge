#by ELO
import os
import csv

filepath = os.path.join("Resources","election_data.csv")
writefilepath = os.path.join("Analysis","ElectionResults.txt")

count_row = 0
total = 0
tempData = []
max_votes = 0
max_votes_name =''
candidateName = []
candidateData = []

#open cvs input file
with open(filepath) as file:
    csvreader = csv.reader(file)
    next(csvreader, None)
    #iterate through the file and copy data to new list
    for row in csvreader:
        #print(row[1])
        tempData.append(row)
        count_row += 1

    #iterate throught the list to find unique candidate names
    for i in range(len(tempData)):
        if tempData[i][2] not in candidateName: 
            candidateName.append(tempData[i][2])

    #main loop to iterate through the list to derive vote numbers per candidate        
    for j in range(len(candidateName)):
        votesNumber = 0
        votesPercentage = 0
        for i in range(len(tempData)):       
            if tempData[i][2] in candidateName[j]:
                votesNumber += 1

        votesPercentage = votesNumber*100/count_row
        tempList = [candidateName[j],votesPercentage,votesNumber]
        candidateData.append(tempList)
    
    #loop to find the winner
    for k in range(len(candidateData)):
        if max_votes < candidateData[k][2]:
            max_votes = candidateData[k][2]
            max_votes_name = candidateData[k][0]
        
#concatenate results into single output variable
output = ("Election Results\n" +
          "-------------------------\n" +
          "Total Votes: "+ str(count_row)+"\n"+
          "-------------------------\n")
for k in range(len(candidateData)):
    output += "{:}:".format(candidateData[k][0]) + " {:,.3f}%".format(candidateData[k][1]) + " ({:})\n".format(candidateData[k][2])
output += ("-------------------------\n"+
           "Winner: "+str(max_votes_name)+"\n"+
           "-------------------------")

# print results in requested format           
print(output)
# open new text file with write access mode
with open(writefilepath,"w",newline='') as txtfile:
    #write results to file in requested format
    txtfile.write(output)
