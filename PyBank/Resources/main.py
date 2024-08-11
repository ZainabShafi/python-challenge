#Your task is to create a Python script that analyzes the records to calculate each of the following values#
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes. 
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

#variables to hold data: months(int), ProfLoss(float), greatestinc(float), greatestdec(float)


#first step is to read csv file budget_data 
import os
import csv

#initialize variable types, greatest inc/dec initialized with poss values
total_months = 0
month_of_change = []
net_change_list = []
#any positive value > 0, will replace greatest_inc with next greatest val. 
#same logic for greatest dec.
greatest_inc = ["", 0]
greatest_dec = ["", 99999999999999]
total_net = 0


# Read CSV file
#for loop doesn't follow conditions - it'll iterate that many times. 
#whileloop - map out every outcome. 
csvpath = ("/Users/zainabshafi/Desktop/python-challenge/PyBank/Resources/budget_data.csv")
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    header = next(csvreader)

    first_row = next(csvreader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:
        total_months += 1
        total_net = int(row[1])

        net_change = total_net - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        if net_change > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = net_change
        if net_change < greatest_dec[1]:
            greatest_dec[0] = row[0]
            greatest_dec[1] = net_change

net_month_avg = sum(net_change_list) / len(net_change_list)

output = (
    f"Financial Analysis\n"
    f"----------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {total_net}\n"
    f"Average Change: {net_month_avg:.2f}\n"
    f"Greatest Inc: {greatest_inc[1]}, month of it: {greatest_inc[0]}\n"
    f"Greatest dec: {greatest_dec[1]}, month of it: {greatest_dec[0]}\n"
)
          
print(output)

with open('PyBank_Analysis.txt', 'w') as file:
    print(output, file=file)
    
        





       
       
    


    
    
   

  
   



     


      
    



    
















  



 

























    
