import os
import csv
import datetime

def get_percentage(numerator, denominator):
    value = (numerator/denominator)*100
    value = round(value, 2)
    return (str(value) + "%")

input_file = os.path.join('election_data_1.csv')

output_file = os.path.join('results.txt')
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

with open(output_file, 'w', newline='') as file:
    # Write the first row (column headers)
    file.write("Election Results\n")
    print("Election Results")
    file.write("-------------------------\n")
    print("-------------------------")
    file.write("Total Votes: " + str(total_votes) +"\n")
    print("Total Votes: " + str(total_votes))
    file.write("-------------------------\n")
    print("-------------------------")
    for politican in master_dict:
        file.write(politican + ": " + get_percentage(master_dict[politican],total_votes)
            + " ("+str(master_dict[politican])+")\n")
        print(politican + ": " + get_percentage(master_dict[politican],total_votes)
            + " ("+str(master_dict[politican])+")")
        if master_dict[politican] > temp:
            temp = master_dict[politican]
            winner = politican
    file.write("-------------------------\n")
    print("-------------------------")
    file.write("Winner: " + winner+"\n")
    print("Winner: " + winner)
    file.write("-------------------------\n")
    print("-------------------------")
