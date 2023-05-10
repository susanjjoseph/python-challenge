import csv

# Path to the CSV file
file_path = "Resources/election_data.csv"

# Define variables
total_votes = 0
candidate_votes = {}
candidates = []
winner_votes = 0
winner = ""

# Read in the CSV file
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None) # skip the header row

    # Loop through the data
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1

        # Add each candidate to a list of candidates
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0

        # Count the number of votes each candidate received
        candidate_votes[candidate] += 1

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print the percentage of votes each candidate won
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    percent_votes = votes / total_votes * 100
    print(f"{candidate}: {percent_votes:.3f}% ({votes})")

    # Determine the winner based on popular vote
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
output_file = "analysis/election_results.txt"
with open(output_file, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percent_votes = votes / total_votes * 100
        outfile.write(f"{candidate}: {percent_votes:.3f}% ({votes})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("-------------------------\n")