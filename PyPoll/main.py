import os 
import csv
election_data = os.path.join('Resources', 'election_data.csv')
election_analysis = os.path.join('analysis', 'election_data.txt')
tot_votes = 0
candidates = []
vote_count = {}
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    csv_header = next(csvreader)
    
    #making seperate lists for candidates and vote count
    for i in csvreader: 
        tot_votes +=1
        candidate = i[2]
        if candidate not in candidates: 
            candidates.append(candidate)
            vote_count[candidate]=0
        vote_count[candidate]+=1
    print(vote_count)
with open(election_analysis,"w") as txt:
    total = (f"""
Election Results
-------------------------
Total Votes: {tot_votes}
-------------------------
""")
    print(total)
    txt.write(total)

    for candidate in vote_count:
        votes = vote_count.get(candidate)
        percent = round(votes/tot_votes*100,3)
        candidate_vote = (f"{candidate}: {percent}% ({votes}) \n")
        print(candidate_vote)
        txt.write(candidate_vote)
    winner = max(vote_count, key= vote_count.get)
    winner_dec = (f"""
-------------------------
Winner: {winner}
-------------------------
    """)
    print(winner_dec)
    txt.write(winner_dec)
   
