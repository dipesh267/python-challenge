import os
import csv
import datetime

def get_state_abv(fname):
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }
    return us_state_abbrev[fname]
    
input_file = os.path.join('employee_data1.csv')

output_file = os.path.join('master1.csv')
master_list = []
with open(input_file, 'r', newline='') as csvfile:
    data_file = csv.reader(csvfile, delimiter=',')
    #skip the first row of the csv becuase it's a header line
    next(data_file, None)

    for row in data_file:
        emp_id = row[0]
        
        name = row[1].split(" ")
        first_name = name[0]
        last_name = name[1]
        
        #dob = datetime.date(row[2])
        dob = datetime.datetime.strptime(row[2], "%Y-%m-%d")
        dob_formatted = str(dob.strftime("%m/%d/%Y"))
        ssn = row[3].split("-")
        ssn_formatted = "xxx-xx-"+ssn[2]
        state = get_state_abv(row[4])
        
        temp_list = [emp_id,first_name,last_name,dob_formatted,ssn_formatted,state]
        master_list.append(temp_list)
        
        #master_dict does get loaded but can't seem to be able to iterate thru it to going the list route.
        #master_dict = {
        #    emp_id : [first_name,last_name,dob_formatted,ssn_formatted,state]
        #}
    #print(master_list[1])

with open(output_file, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

    for name in master_list:
        csvwriter.writerow([name[0],name[1],name[2],name[3],name[4],name[5]])