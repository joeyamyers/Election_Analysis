# add our dependencies
import csv
import os
#assign a var to load the file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# assign a var to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election results and read file
with open(file_to_load) as election_data:
    # read the file object with the reader function
    file_reader = csv.reader(election_data)
   
    # read and print the header row
    headers = next(file_reader)
    print(headers)

    #print ea row in csv file
    for row in file_reader:
        print(row)








# using the with statement open the file as a text file
# with open(file_to_save, "w") as txt_file:
    #txt_file.write("Hello")





# data we need to retrieve
# 1 total number of votes cast
# 2 complete list of candidates who received votes
# 3 percentage of votes each candidate won
# 4 total number of votes cast for each candidate
# 5 the winner of the election based on popular vote