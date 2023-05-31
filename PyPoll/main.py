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
        tot_votes +=1 #getting the total amount of votes
        candidate = i[2] #declaring the cadidate row
        if candidate not in candidates: #if the name isn't on the list add it onto it
            candidates.append(candidate) #putting it into a list
            vote_count[candidate]=0 #setting the vote count to zero
        vote_count[candidate]+=1 #getting the count for each candidate
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
        votes = vote_count.get(candidate) #getting the vote total for each candidate
        percent = round(votes/tot_votes*100,3) #getting percent
        candidate_vote = (f"{candidate}: {percent}% ({votes}) \n") 
        print(candidate_vote)
        txt.write(candidate_vote)
    winner = max(vote_count, key= vote_count.get) #finding the winner via max
    winner_dec = (f"""
-------------------------
Winner: {winner}
-------------------------
    """)
    print(winner_dec)
    txt.write(winner_dec)
   
