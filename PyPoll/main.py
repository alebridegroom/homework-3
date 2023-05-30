import os 
import csv
election_data = os.path.join('Resources', 'election_data.csv')
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    csv_header = next(csvreader)
    tot_votes = []
    candidates = []
    #making seperate lists for candidates and vote count
    for i in csvreader:
        tot_votes.append(i[0])
        candidates.append(i[2])
    #total amount of votes
    tote_votes = len(tot_votes)
    #unique values of the candidates row using set() and putting it in a list
    candidates_set = list(set(candidates))
    
    #getting the count for each candidate of votes via the references of the rows in the unique value list
    c_votes = candidates.count(candidates_set[0])
    d_votes = candidates.count(candidates_set[1])
    r_votes = candidates.count(candidates_set[2])
    vote_max = [c_votes,d_votes,r_votes]
    #zipping the votes in ad dictionary in order to get the max amount
    zip_count = dict(zip(candidates_set,vote_max))
    
    #finding the percent amount of each candidate
    c_percent = round((c_votes/tote_votes)*100,3)
    d_percent = round((d_votes/tote_votes)*100,3)
    r_percent = round((r_votes/tote_votes)*100,3)
    
    #finding the winnder using max() fuanction with the key being .get
    winner = max(zip_count, key=zip_count.get)
    
    
    
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {tote_votes}")
    print("--------------------------")
    print(f"{candidates_set[0]}: {c_percent}% ({c_votes})")
    print(f"{candidates_set[1]}: {d_percent}% ({d_votes})")
    print(f"{candidates_set[1]}: {r_percent}% ({r_votes})")
    print("--------------------------")
    print(f"Winner: {winner}")