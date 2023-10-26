# read the CSV file
import os
import csv
bank_csv = os.path.join("Resources","budget_data.csv")
# Working fields
tot_months = 0
tot_profit_loss = 0
delta_profit_loss = 0 
tot_delta = 0
avg_delta = 0     
greatest_increase = 0
increase_date = []
greatest_decrease = 0
decrease_date = []
sv_profit_loss = 0
# open and read header
with open(bank_csv, encoding="UTF-8") as bankfile:
    csvreader = csv.reader(bankfile, delimiter=",")
    csv_header = next(csvreader)
    # loop through file
    for row in csvreader:
        # The total number of months included in the dataset
        tot_months = tot_months + 1
        # The net total amount of "Profit/Losses" over the entire period
        tot_profit_loss = tot_profit_loss + int(row[1])
        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        if tot_months > 1:
            delta_profit_loss = (sv_profit_loss - int(row[1])) * -1 
            tot_delta = tot_delta + delta_profit_loss  
            sv_profit_loss = int(row[1])
        else:    
            sv_profit_loss = int(row[1])
        # The greatest increase in profits (date and amount) over the entire period
        if delta_profit_loss > greatest_increase:
            greatest_increase = delta_profit_loss
            increase_date = row[0]
        # The greatest decrease in profits (date and amount) over the entire period
        if delta_profit_loss < greatest_decrease:
            greatest_decrease = delta_profit_loss
            decrease_date = row[0]
# average Change
from decimal import Decimal
avg_delta = Decimal(tot_delta / (tot_months - 1)).quantize(Decimal("0.00"))
# open file and write to it
row1 = f'Financial Analysis\n'
row2 = f'-------------------------------------\n'
row3 = f'Total Months:  {tot_months}\n'  
row4 = f'Total: ${tot_profit_loss}\n' 
row5 = f'Average Change:  ${avg_delta}\n' 
row6 = f'Greatest Increase in Profits: {increase_date} (${greatest_increase})\n'
row7 = f'Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n'
output_file = os.path.join("analysis", "Financial_Analysis.txt")
with open(output_file, "w", newline = '\n') as datafile:
    datafile.write(row1)    
    datafile.write(row2)
    datafile.write(row3) 
    datafile.write(row4)
    datafile.write(row5)
    datafile.write(row6)
    datafile.write(row7)
# print the results
print(f'Financial Analysis')
print(f'-------------------------------------')
print(f'Total Months: ' ,    tot_months)  
print(f'Total: ', '$' , tot_profit_loss,sep='') 
print(f'Average Change: $',avg_delta, sep='') 
print(f'Greatest Increase in Profits: ',increase_date, ' ($', greatest_increase, ')', sep='')
print(f'Greatest Decrease in Profits: ',decrease_date, ' ($', greatest_decrease, ')', sep="")