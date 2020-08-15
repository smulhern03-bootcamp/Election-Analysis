#add our dependencies
import csv
import os
# Assign a variable to laod a file from a path.
electionresults = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
electionanalysis= os.path.join("analysis", "election_analysis.txt")

#1. Initialize vote counter, candidate options, candidate votes, winnings
total_votes = 0

# Candidate Options
candidate_options = []

#Candidate Votes
candidate_votes = {}

#Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the elction results and read the file.
with open(electionresults) as election_data:
    file_reader = csv.reader(election_data)
    
    #Read the header row
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes +=1    
        
        # Print the candidate name from each row.
        candidate_name = row [2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        
        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1
    #writing to text file
    with open(electionanalysis, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"---------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"---------------------------\n")
        print(election_results, end ="")
        #save the final voute count to the text file.
        txt_file.write(election_results)
            #Each candidate's percentage of vote.
            #vote_percentage = (votes/total_votes)*100
        for candidate_name in candidate_votes:
                #retrieve vote count of a candidate.
                    votes = candidate_votes[candidate_name]
                    #print(candidate_name, votes)
                #Calculate the precentage of votes
                    vote_percentage = float(votes)/ float(total_votes)*100
                    #print(candidate_name, vote_percentage)
                #Print the candidate name and percentage of votes
                    #print(f"{candidate_name}: receieved {(format(vote_percentage, '.1f'))}% of the vote.")
                    if (votes > winning_count) and (vote_percentage > winning_percentage):
                        winning_count = votes
                        winning_percentage = vote_percentage
                        winning_candidate = candidate_name
                    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
                    print(candidate_results)
                    txt_file.write(candidate_results)
        winning_candidate_summary = (
            f"                       \n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"                       \n")
        txt_file.write(winning_candidate_summary)
        #print(winning_candidate_summary)

    # Print the total votes.
        #print(candidate_options)
        #print(total_votes)
        #print(candidate_votes)