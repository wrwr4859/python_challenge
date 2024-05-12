import os
import csv

#path to budget data

bank_csv = r'/Users/wenlirui/Desktop/python_challenge/PyBank/Resources/budget_data.csv'

#List Store data
months = []
average_change_list = []

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
    
    #initiate greatest profit increase calc and date tracker
    greatest_profit_increase = 0
    greatest_profit_increase_date = ""
    
    #initiate greatest profit decrease calc and date tracker
    greatest_profit_decrease = 0
    greatest_profit_decrease_date = ""

    # loop through each row
    for row in csvreader:
        #get the month data in each row
        month = row[0]
        #add profit loss to profit loss calc
        profit_loss = profit_loss+ int(row[1])
        #append the month data in each row to the list
        months.append(month)

        #track profit and loss in each row and append to list
        average_change_list.append(int(row[1]))
    

        #track greatest profit increase
        if int(row[1]) > greatest_profit_increase:
            greatest_profit_increase = int(row[1])
            greatest_profit_increase_date = (row[0])
        else:
            greatest_profit_increase = greatest_profit_increase
            greatest_profit_increase_date = greatest_profit_increase_date

        #track greatest profit decrease
        if int(row[1]) < greatest_profit_decrease:
            greatest_profit_decrease = int(row[1])
            greatest_profit_decrease_date = (row[0])
        else:
            greatest_profit_decrease = greatest_profit_decrease
            greatest_profit_decrease_date = greatest_profit_decrease_date

#loop through profit and loss list and calc the change in profit and loss and append that to a new list
average_change_list2 = []
for i in range(len(average_change_list)):
    if i == 0:
        #skip
        pass
    else:
        average_change = average_change_list[i] - average_change_list[i-1]
        average_change_list2.append(average_change)

#calculate the average change with formatting
Sum = sum(average_change_list2)
Average_Change = Sum / len(average_change_list2)
Average_Change_Formatted = "%1.2f" % Average_Change


#print results
print ("Financial Analysis")
print("----------------------")
print("Total Months: " + str(len(months)))
print("Total: $" + str(profit_loss))
print("Average Change: $" + (str(Average_Change_Formatted)))
print("Greatest Increase in Profits: " + greatest_profit_increase_date + " ($" + str(greatest_profit_increase) + ")")
print("Greatest Decrease in Profits: " + greatest_profit_decrease_date + " ($" + str(greatest_profit_decrease) + ")")

#write results to a new file
f = open("/Users/wenlirui/Downloads/PyBank.txt", "a")
f.write("Financial Analysis")
f.write("\n----------------------")
f.write("\nTotal Months: " + str(len(months)))
f.write("\nTotal: $" + str(profit_loss))
f.write("\nAverage Change: $" + str(Average_Change_Formatted))
f.write("\nGreatest Increase in Profits: " + greatest_profit_increase_date + " ($" + str(greatest_profit_increase) + ")")
f.write("\nGreatest Decrease in Profits: " + greatest_profit_decrease_date + " ($" + str(greatest_profit_decrease) + ")")
f.close()




