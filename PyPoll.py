# add our dependencies
import csv
import os
#assign a var to load the file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# assign a var to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize a total vote count
total_votes = 0

# Candidate options and votes
candidate_options = []
# empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read file
with open(file_to_load) as election_data:
    # read the file object with the reader function
    file_reader = csv.reader(election_data)
   
    # read and print the header row
    headers = next(file_reader)
    print(headers)

    #print ea row in csv file
    for row in file_reader:
        # add to the total vote count
        total_votes += 1
       
        # print the candidate name from each row
        candidate_name = row[2]
        
        # add candidate name to candidate options list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
    # print the final count to to the terminal
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")
    print(election_results, end="")
    # save the final vote count to the text file
    txt_file.write(election_results)

    # Determine percentage of votes per candidate by looping through the counts
    # loop through the candidate list
    for candidate_name in candidate_votes:
        # retreieve vote count of each candidate
        votes = candidate_votes[candidate_name]
        # calculate percentage of votes and convert to floats
        vote_percentage = (float(votes)/float(total_votes)) * 100
        
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)
        # save the candidate results to our text file
        txt_file.write(candidate_results)


        # Determine winning vote count and candidate
        # determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true, then these are equal
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)