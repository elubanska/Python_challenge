#by ELO
import os
import csv

filepath = os.path.join("Resources","budget_data.csv")
writefilepath = os.path.join("Analysis","Financial_Analysis.txt")

count_row = 0
total = 0
min_val = 0
max_val = 0
tempData = []
avgChange = 0

#open cvs input file
with open(filepath) as file:
    csvreader = csv.reader(file)
    next(csvreader, None)
    #iterate through the file and copy data to new list
    for row in csvreader:
        #print(row[1]) 
        tempData.append(row)
        count_row += 1
        total += int(row[1])
    
    i = 0
    #main loop to iterate through the list to derive requested change values
    for i in range(len(tempData)-1):
        if min_val > (int(tempData[i+1][1])-int(tempData[i][1])):
            min_val = (int(tempData[i+1][1])-int(tempData[i][1]))
            min_month = tempData[i+1][0]
        if max_val < (int(tempData[i+1][1])-int(tempData[i][1])):
            max_val = (int(tempData[i+1][1])-int(tempData[i][1]))
            max_month = tempData[i+1][0]
        avgChange +=(int(tempData[i+1][1])-int(tempData[i][1]))
        i += 1

#concatenate output results
output = "Financial Analysis\n----------------------------\nTotal Months: {}\nTotal: ${:}\nAverage Change: ${:.2f}\nGreatest Increase in Profits: {} (${:})\nGreatest Decrease in Profits: {} (${:})\n" 
# print results in requested format
print(output.format(count_row,total,avgChange/i,max_month,max_val,min_month,min_val))

# open new text file with write access mode
with open(writefilepath,"w",newline='') as txtfile:
    #write results to file in requested format
    txtfile.write(output.format(count_row,total,avgChange/i,max_month,max_val,min_month,min_val))
