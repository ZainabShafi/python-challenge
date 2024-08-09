#The total number of votes cast
#A complete list of candidates who received votes
#The total number of votes each candidate won
#The percentage of votes each candidate won
#The winner of the election based on popular vote

import os 
import csv 
total_votes = 0
cand_list = []
perc_vote_cand = {}
total_votes_cand = {}
election_winner = []


csvpath = os.path.join("/Users/zainabshafi/Desktop/python-challenge/PyPoll/Resources/election_data.csv")
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    header = next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        cand = row[2]
        if cand not in cand_list:
            cand_list.append(cand)
            total_votes_cand[cand] = 0
        total_votes_cand[cand] = total_votes_cand[cand] +1
        perc_vote_cand[cand] = f"{round(total_votes_cand[cand]/total_votes*100,2)}%"

       
    

        
print("The candidates are:",cand_list)  
print("Total votes cast are:",total_votes)
print("The total votes for each candidate are:",total_votes_cand)
print("The percentage of votes each candidate won:",perc_vote_cand)
print("The winner of the election is:", max(total_votes_cand,key=total_votes_cand.get))

file = open("Analysis/Pypoll_Analysis.txt", 'w')
