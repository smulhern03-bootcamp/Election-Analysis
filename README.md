# Election-Analysis
## Election Audit Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the elction based on popular vote.
- Additional Tasks
6. Calculate voter turnout per county.
7. Calculate percentage of votes out of each county's total votes.
8. Determine county with the highest turnout.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7, Virtual Studio Code, 1.48

## Results of Audit
 There were a total of 369,711 total votes cast in this congressional district election. 
The county breakdown of votes is as follows:
  Denver: 82.8% (306,055)
  Jefferson: 10.5% (38,855)
  Arapahoe: 6.7% (24,801)
Denver county had the largest number of votes by a large margin.
For the candidates for the seat, Diana DeGette won the majority of votes with 272,892 total votes, 73.8% of the votes cast.  Charles Casper Stockham received 85,213, 23% of the votes, while Raymon Anthony Doane received 11,606 or 3.1% of the votes.

## Summary
The PyPoll code, written in Python, can be useful other elections - government or not.  A basic modification can be to the code relating to the counties.  While the code used was specific to one congressional district, with some modifications, the code could be used for elections for other districts or state-wide elections.  The key is to change the "county' label in county_list and county_votes to whatever unit of analysis is necessary.  For example:

        district_list = []
        district_votes = {}
       
        if district_name is not in district_list:
            district_list.append(district_name)
            district_votes[district_name] = 0
        district_votes[district_name] += 1
        
Similiar to the modification for counties, demographics could be modified into the code:

        ethnicity_list = []
        ethnicity_votes = {}
        
        if ethnicity_name is not in ethnicity_list:
            ethnicity_list.append(ethnicity_name)
            ethnicity_votes[ethnicity_name] = 0
        ethnicity_votes[ethnicity_name] += 1
       
Further modifications could be made to determine lowest voter turnout or analysis of demographics.  
       
       smallest_count = 0
       smallest_county = ""
       
       for county_name in county_votes:
            votes = county_votes[county_name]
            vote_percentage = float(votes)/ float(total_votes)*100
            if (votes > smallest_count):
             smallest_count = votes
             smallest_county = county_name

Just as the county coding was modified from the candidate-centric code, the same small modifications could be made for demographics.  Depending on what data is provided.  The code can be modified to fit the research question.
