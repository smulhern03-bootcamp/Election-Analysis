#The data we need to retrieve
#1. the total nmber of votes cast
#2. a complete list of condidates who received votes
#3. the percentage of votes each candidate won
#4. the total number of votes each candidate won
#5. the winner of the election based on popular vote
#electionresults = 'Resources/election_results.csv'
#election_data = open(electionresults, 'r')
#election_data.close()
#with open(electionresults) as election_data:
    #print(election_data)
import csv
import os
electionresults = os.path.join("Resources", "election_results.csv")
electionanalysis= os.path.join("analysis", "election_analysis.txt")
with open(electionresults) as election_data:
    file_reader = csv.reader(election_data)
    #for row in file_reader:
       # print(row)
    headers = next(file_reader)
    print(headers)