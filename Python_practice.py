voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
#for county_dict in voting_data:
    #print(county_dict)
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict:
   # print(county)    
for county, voters in voting_data.value():
    #print(county, "county has", voters, "registered voters.")
    #for value in county_dict.values():
        print(f"{county} county has {voters} registered voters.")
        