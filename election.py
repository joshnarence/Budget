#Importing modules
import csv
import os

#Defining the path to file
electioncsv =os.path.join("C:/Users/Joshna Rence/Desktop/Data Analytics/election_data.csv")

#Setting variables
count = 0
name = []
candidate = []
vote_count = []
vote_percent = []

# Giving access to my file
with open(electioncsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # reading the information by row
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to name
        name.append(row[2])
        # Get the unique candidate names
    for x in set(name):
        candidate.append(x)
        # y is the total number of votes per candidate
        y = name.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote = max(vote_count)
    winner = candidate[vote_count.index(winning_vote)]
    sorted_candidate = sorted(candidate)
    
# Printing the results
print("Election Results")   
print("-------------------------")
print(f"Total Votes : {count}")    
print("-------------------------")
for i in range(len(sorted_candidate)):
    print(f"{sorted_candidate[i]} : {round(vote_percent[i])} % {vote_count[i]}")
print("-------------------------")
print(f"The winner is:  {winner}")
print("-------------------------")
# Creating path to file
output = os.path.join("C:/Users/Joshna Rence/Desktop/Data Analytics/electonresults.txt")
# Creating text file 
with open(output, "w") as file:
    writer = csv.writer(file)
    file.write("Election Results\n") 
    file.write("-------------------------\n")
    file.write(f"Total Votes : {count}\n")
    for i in range(len(sorted_candidate)):
        file.write(f"{sorted_candidate[i]} : {round(vote_percent[i])} % {vote_count[i]}\n")
    file.write("-------------------------\n")
    file.write(f"The winner is:  {winner}\n")
    file.write("-------------------------\n")

#with open(output, "w") as file:
    #print("Election Results", file)   
    #print("-------------------------", file)
    #print(f"Total Votes : {count}", file)    
    #print("-------------------------", file)
    #for i in range(len(sorted(candidate))):
        #print(candidate[i] + ": " + str(round(vote_percent[i])) +"% (" + str(vote_count[i])+ ")", file)
    #print("-------------------------", file)
    #print(f"The winner is:  {winner}", file)
    #print("-------------------------", file)