#PyPoll Main.py

#first we import
import os
import csv

#create our pathway
elecdata_csv = os.path.join('Resources', 'election_data.csv')

#create an empty list for voter IDs so we can count them for total voter count
voter_id_list = []
khan_votes = []
correy_votes = []
tooley_votes = []
li_votes = []

#open and read csv file
with open(elecdata_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)

    #begin for loop through csv
    for row in csvreader:

        #count all the voter ID's
        voter_id_list.append(row[0])

        #if statement to collect votes for each candidate
        if row[2] == 'Khan':
            khan_votes.append(row[2])
        elif row[2] == 'Correy':
            correy_votes.append(row[2])
        elif row[2] == "O'Tooley":
            tooley_votes.append(row[2])
        elif row[2] == 'Li':
            li_votes.append(row[2])

#get percentages of each voter
khan_percent = len(khan_votes) / len(voter_id_list) * 100     
correy_percent = len(correy_votes) / len(voter_id_list) * 100
tooley_percent = len(tooley_votes) / len(voter_id_list) * 100
li_percent = len(li_votes) / len(voter_id_list) * 100

#dictionary of votes
electionresults = {
    'Khan': (khan_percent),
    'Correy': (correy_percent),
    "O'Tooley": (tooley_percent),
    'Li': (li_percent)}

#decide winner(source: https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python)
winner = max(electionresults, key=electionresults.get)

# #print statement to test results of code
# print(f'Total votes is: {len(voter_id_list)}')
# print(f'Total votes for Khan is: {len(khan_votes)}')
# print(f"Total votes for O'Tooley is: {len(tooley_votes)}")
# print(f'Total votes for Li is: {len(li_votes)}')
# print(f'Total votes for Correy is: {len(correy_votes)}')
# print(f'Khan percentage is %{round(khan_percent, 4)}')

print("Election Results")
print('------------------------------')
print(f'Total Votes: {len(voter_id_list)}')
print('------------------------------')
print(f'Khan: {round(khan_percent, 4)}% ({len(khan_votes)})')
print(f'Correy: {round(correy_percent, 4)}% ({len(correy_votes)})')
print(f"O'Tooley: {round(tooley_percent, 4)}% ({len(tooley_votes)})")
print(f'Li: {round(li_percent, 4)}% ({len(li_votes)})')
print('------------------------------')
print(f'Winner: {winner}')
print(f'-----------------------------')


#Create link for output csv
Output_csv = os.path.join('Analysis', 'Output_csv.csv')

with open(Output_csv, "w") as file:
    file.write('Election Results')
    file.write('\n')
    file.write('---------------------------')
    file.write('\n')
    file.write(f'Total Votes: {len(voter_id_list)}')
    file.write('\n')
    file.write('---------------------------')
    file.write('\n')
    file.write(f'Khan: {round(khan_percent, 4)}% ({len(khan_votes)})')
    file.write('\n')
    file.write(f'Correy: {round(correy_percent, 4)}% ({len(correy_votes)})')
    file.write('\n')
    file.write(f"O'Tooley: {round(tooley_percent, 4)}% ({len(tooley_votes)})")
    file.write('\n')
    file.write(f'Li: {round(li_percent, 4)}% ({len(li_votes)})')
    file.write('\n')
    file.write('---------------------------')
    file.write('\n')
    file.write(f'Winner: {winner}')
    file.write('\n')
    file.write('---------------------------')
