import os
import csv

#path to budget data

bank_csv = r'/Users/wenlirui/Desktop/python_challenge/PyBank/Resources/budget_data.csv'

#List Store data
months = []
changes = []

# Open the CSV file
with open(bank_csv, newline='', encoding='utf-8') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row (if there is one)
    next(csvreader)

    #initiate profit loss calc
    profit_loss = 0
    #average change calc initiation
    average_change = 0

    #intiate previous row tracker
    prev_row = 0

    # loop through each row
    for row in csvreader:
        #get the month data in each row
        month = row[0]
        #add profit loss to profit loss calc
        profit_loss = profit_loss+ int(row[1])
        #append the month data in each row to the list
        months.append(month)

        #track change in profit and loss
        change = int(row[1]) - prev_row
        prev_row = int(row[1])
        changes.append(change)

#calculate the average change with formatting
del changes[0]
Sum = sum(changes)
Average_Change = Sum / (len(changes))
Average_Change_Formatted = "%1.2f" % Average_Change

#find the index of max profit increase/decrease
index_max = changes.index(max(changes))
index_min = changes.index(min(changes))

#print results
print ("Financial Analysis")
print("----------------------")
print("Total Months: " + str(len(months)))
print("Total: $" + str(profit_loss))
print("Average Change: $" + (str(Average_Change_Formatted)))
print("Greatest Increase in Profits: " + months[index_max+1] + " ($" + str(max(changes))+ ")")
print("Greatest Decrease in Profits: " + months[index_min+1] + " ($" + str(min(changes)) + ")")

# write results to a new file
f = open("/Users/wenlirui/Desktop/python_challenge/PyBank/Analysis/PyBank.txt", "a")
f.write("Financial Analysis")
f.write("\n----------------------")
f.write("\nTotal Months: " + str(len(months)))
f.write("\nTotal: $" + str(profit_loss))
f.write("\nAverage Change: $" + str(Average_Change_Formatted))
f.write("\nGreatest Increase in Profits: " + months[index_max+1] + " ($" + str(max(changes))+ ")")
f.write("\nGreatest Decrease in Profits: " + months[index_min+1] + " ($" + str(min(changes))+ ")")
f.close()




