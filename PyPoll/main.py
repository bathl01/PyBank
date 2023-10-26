# read the CSV file
import os
import csv
poll_csv = os.path.join("Resources","election_data.csv")
# Working fields
tot_cast = 0
perc_votes = 0
candidate_vote = 0
candidate_dict = {}
candidate_list = []
# Import Python moduels 
from decimal import Decimal
from collections import Counter
# open and read header
with open(poll_csv, encoding="UTF-8") as pollfile:
    csvreader = csv.reader(pollfile, delimiter=",")
    csv_header = next(csvreader)
 
    # loop through file
    for row in csvreader:
        # The total number of votes cast
        tot_cast = tot_cast + 1
        # A complete list of candidates who received votes
        candidate_list.append(row[2]) 
    for ele in candidate_list:
        if ele in candidate_dict:
            candidate_dict[ele] += 1
        else:
            candidate_dict[ele]=1
output_file = os.path.join("Analysis", "Election_Results.txt")
with open(output_file, "w", newline = '\n') as datafile:
    head_row = f'Election Results\n'
    dash_row = f'-------------------------------------\n'
    tot_row = f'Total Votes:  {tot_cast} \n' 
    print(head_row)
    datafile.write(head_row) 
    print(dash_row)
    datafile.write(dash_row) 
    print(tot_row)
    datafile.write(tot_row) 
    print(dash_row)
    datafile.write(dash_row) 
    # create and print detail records
    for key,ele in candidate_dict.items():      
        # The percentage of votes each candidate won - print & write
        candidate_vote = ele
        perc_votes = Decimal(candidate_vote / tot_cast *100).quantize(Decimal("0.000"))
        det_row=f'{key}:  {perc_votes}% ({ele})\n'
        print(det_row,sep='' )
        datafile.write(det_row) 
      
    # The winner of the election based on popular vote
    cand = list(candidate_dict.keys())
    cand_vote = list(candidate_dict.values())
    max_index = cand_vote.index(max(cand_vote))
    winner = list(cand)[max_index]

    # print & write the rest of the report
    print(dash_row)
    datafile.write(dash_row)
    win_row = f'Winner: {winner}\n'
    print(win_row)
    datafile.write(win_row)
    print(dash_row)
    datafile.write(dash_row)