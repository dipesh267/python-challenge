import os
import csv
import datetime

file_path = os.path.join('budget_data_1.csv')
output_file = os.path.join('results.txt')
master_list = []
yearly_dict = dict()

total_revenue = 0
total_months = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

with open(file_path,'r',newline='') as csvfile:
    data_file = csv.reader(csvfile, delimiter=',')

    #skip the first line
    next(data_file, None)

    for row in data_file:
        #looking to see what format the date is in.
        total_months += 1
        temp = row[0].split("-")
        if(len(temp[1])== 4):
            input_format = "%b-%Y"
        else:
            input_format = "%b-%y"

        rev_date = datetime.datetime.strptime(row[0], input_format)
        rev_year = rev_date.year
        rev_month = rev_date.month
        revenue = int(row[1])
        
        if revenue > greatest_increase:
            greatest_increase = revenue
            greatest_increase_date = rev_date.strftime("%b-%y") 
        
        if revenue < greatest_decrease:
            greatest_decrease = revenue
            greatest_decrease_date = rev_date.strftime("%b-%y")

        total_revenue += revenue
        
        master_list.append([rev_year, rev_month, revenue])

average_revenue = '{0:.2f}'.format(total_revenue/total_months)
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: $" + str(total_revenue))
print("Average Renevue Change: $" + str(average_revenue))
print("Greatest Increase in Revenue: " + greatest_increase_date + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Reveneu: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")")

with open(output_file, 'w', newline='') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write("Total Months: " + str(total_months) + "\n")
    file.write("Total Revenue: $" + str(total_revenue) + "\n")
    file.write("Average Renevue Change: $" + str(average_revenue) + "\n")
    file.write("Greatest Increase in Revenue: " + greatest_increase_date + " ($" + str(greatest_increase) + ")\n")
    file.write("Greatest Decrease in Reveneu: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")\n")
