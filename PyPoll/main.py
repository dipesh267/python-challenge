import os
import csv
import datetime
    
input_file = os.path.join('election_data_1.csv')

output_file = os.path.join('results.csv')
master_dict = {}
total_votes = 0
winner = ""
temp = 0

with open(input_file, 'r', newline='') as csvfile:
    data_file = csv.reader(csvfile, delimiter=',')
    #skip the first row of the csv becuase it's a header line
    next(data_file, None)

    for row in data_file:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        total_votes = total_votes + 1
        #dictionary of candidate and their vote count
        if candidate in master_dict:
            x = master_dict[candidate]
            master_dict[candidate] = x+1
            x = 0
        else:
            master_dict[candidate] = 1

with open(output_file, 'w', newline='') as csvfile:
    # Write the first row (column headers)
    csvfile.write("Election Results\n")
    print("Election Results")
    csvfile.write("-------------------------\n")
    print("-------------------------")
    csvfile.write("Total Votes: " + str(total_votes) +"\n")
    print("Total Votes: " + str(total_votes))
    csvfile.write("-------------------------\n")
    print("-------------------------")
    for politican in master_dict:
        csvfile.write(politican + ": " + str(master_dict[politican])+"\n")
        print(politican + ": " + str(master_dict[politican]))
        if master_dict[politican] > temp:
            temp = master_dict[politican]
            winner = politican
    csvfile.write("-------------------------\n")
    print("-------------------------")
    csvfile.write("Winner: " + winner+"\n")
    print("Winner: " + winner)
    csvfile.write("-------------------------\n")
    print("-------------------------")