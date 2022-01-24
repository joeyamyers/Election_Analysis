# Election_Analysis

## Project Overview
The Colorado Board of Elections has asked me to complete an audit of the tabulated results for a U.S. Congressional precinct. They have asked for the following tasks to be completed:

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote

### Resources
- Data Source: election_results.csv
- Software: Python 3.9.7, Visual Studio Code, 1.63.2

### Election-Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane

- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.

- The winner of the election was:
    - Candidate 2, Diana DeGette, who received 73.8% of the vote and 272,892 votes.


## Challenge Overview
The election committee has asked for the following additional information:
 1. The voter turnout for each county
 2. The percentage of votes from each county out of the total count
 3. The county with the highest turnout.

### Election-Audit Additional Results
1. The county results were:
    - Arapahoe received 6.7% of the voter turnout and 24,801 votes.
    - Denver received 82.8% of the voter turnout and 306,055 votes.
    - Jefferson received 10.5% of the voter turnout and 38,855 votes.

2. The county with the highest turnout was:
    - Denver which received 82.8% of the voter turnout and 306,055 votes.

### Election-Audit Summary
This script completed the election audit of this Congressional precinct, but arguably could be now used for any election given a few modifications. The key to its versatility is that it was not hardcoded to include the specific county or candidate names for this given election. For a larger-scale election, this script could be modified to include information regarding voter turnout on the state or national level. It could also be modified to be a non-political election script and used for elections of all kinds.
