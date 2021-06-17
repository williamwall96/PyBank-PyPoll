#imports
import os
import csv

#Create path
PyBank_csv = os.path.join('Resources', 'budget_data.csv')

#empty list for each month so that we can count it later
totalMonthList = []

#empty list for net total amount of profit/losses
totalnetrevenue = []

#empty list for average change of profit/losses
profitchange = []

#Read through the csv
with open(PyBank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)

    #For loop to read through each row of data after header
    for row in csvreader:
        
        #get count of total months
        month = row[0]
        
        totalMonthList.append(month)

        #get revenue value of each row
        revenue = row[1]

        totalnetrevenue.append(int(revenue))

    #Read through profits in each row to calculate monthly profit change
    for i in range(len(totalnetrevenue)-1):

        #we take the difference of two months and append that to the profitchange list
        profitchange.append(totalnetrevenue[i+1]-totalnetrevenue[i])

        meanProfitChange = (sum(profitchange)) / (len(profitchange))

#pull the max and min values from the profitchange list
profitchange_max = max(profitchange)
profitchange_min = min(profitchange)

#Now we need to pull the month value, the corresponding month comes 1 after the change we see
profitchangeMaxMonth = profitchange.index(max(profitchange)) + 1
profitchangeMinMonth = profitchange.index(min(profitchange)) + 1
              
#The print statements I made while working on the code to check my work
    # print(f'There are {len(totalMonthList)} total months of data.')
    # print(f'{sum(totalnetrevenue)}')
    # print(f'{round(meanProfitChange, 2)}')
    # print(profitchange_max)
    # print(profitchange_min)

#Print out financial analysis
print('Financial Analysis:')
print('------------------------------')
print(f'Total Months: {len(totalMonthList)}')
print(f'Total Net Revenue: ${sum(totalnetrevenue)}')
print(f'Average change of monthly difference: ${round(meanProfitChange, 2)}')
print(f'Greatest Increase in Profits: {totalMonthList[profitchangeMaxMonth]} (${profitchange_max})')
print(f'Greatest Decrease in Profits: {totalMonthList[profitchangeMinMonth]} (${profitchange_min})')


#Create Output CSV file to print results to

Output_CSV = os.path.join('Analysis', 'Output_PyBank.csv')

with open(Output_CSV,"w") as file:

    #write results into output csv
    file.write('Financial Analysis')
    file.write("\n")
    file.write('=================================')
    file.write("\n")
    file.write(f'Total Months: {len(totalMonthList)}')
    file.write("\n")
    file.write(f'Total Net Revenue: ${sum(totalnetrevenue)}')
    file.write("\n")
    file.write(f'Average change of monthly difference: ${round(meanProfitChange, 2)}')
    file.write("\n")
    file.write(f'Greatest Increase in Profits: {totalMonthList[profitchangeMaxMonth]} (${profitchange_max})')
    file.write("\n")
    file.write(f'Greatest Decrease in Profits: {totalMonthList[profitchangeMinMonth]} (${profitchange_min})')
    file.write("\n")



   
