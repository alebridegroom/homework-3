import os
import csv

#budget_date = os.path.join("/Users/alejandrabridegroom/Desktop/homework AB/homework 3/PyBank","budget_data.csv")
budget_date = os.path.join('Resources', 'budget_data.csv')
with open(budget_date) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    csv_header = next(csvreader)
    #making data as a list so no need to append each row into a seperate list
    #budget_data = list(csvreader)
    
    tot_months = []
    profit = []
    for i in csvreader:
        tot_months.append(i[0])
        profit.append(int(i[1]))

    
    #    total months
    tote_months = len(tot_months) #length of the data set would be the total months
    #total profit
    profit_total = sum(profit)
    
    
    changes = [] #making the changes be its own list so we can sum and divide to find the average
    for i in range(1,tote_months):#makeing it start at the second element of the list
        changes.append(int(profit[i])-int(profit[i-1])) #subtracting the second element from the first through the loopp
    changes_profit = round(sum(changes)/len(changes),2) #finding the average
    max_profit = max(changes) #finding the max
    maxprofit_date = tot_months[changes.index(max_profit)+1] #finding the data of the max using the indexof where the number of where the max is located
    min_profit = min(changes) #finding the min
    minprofit_date = tot_months[changes.index(min_profit)+1] #finding the data of the min using the index of where the number of where the min is located
    
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {tote_months}")
    print(f"Total: ${profit_total}")
    print(f"Average Change: {changes_profit}")
    print(f"Greatest Increase in Profits: {maxprofit_date} (${(str(max_profit))})")
    print(f"Greatest Decrease in Profits: {minprofit_date} (${(str(min_profit))})")
