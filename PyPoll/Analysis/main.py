import os
import csv

#path to budget data

pypoll_csv = r'/Users/wenlirui/Desktop/python_challenge/PyPoll/Resources/election_data.csv'

#List Store data
votes_count = [] #vote count list
#Initiate candidate vote track
Stockham_count = 0
DeGette_count = 0
Doane_count = 0


# Open the CSV file
with open(pypoll_csv, newline='', encoding='utf-8') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row (if there is one)
    next(csvreader)

    for row in csvreader:
        #get the vote ID in each row
        vote_id = row[0]
        #append vote ID to vote count list
        votes_count.append(vote_id)

        #get the vote result in each row
        vote_result = row [2]

        #candidate vote tracker:
        if vote_result == "Charles Casper Stockham":
            Stockham_count = Stockham_count + 1
        if vote_result == "Diana DeGette":
            DeGette_count = DeGette_count + 1
        if vote_result == "Raymon Anthony Doane":
            Doane_count = Doane_count + 1
        else:
            pass

Stockham_percent = "{: .3%}" .format(Stockham_count / len(votes_count))
DeGette_percent = "{: .3%}" .format(DeGette_count / len(votes_count))
Doane_percent = "{: .3%}" .format(Doane_count / len(votes_count))

#use a dict to track each candidate's vote and find who has max votes
Winner_Dict = {"Charles Casper Stockham": Stockham_count, "Diana DeGette": DeGette_count, "Raymon Anthony Doane": Doane_count}
max_winner = max(Winner_Dict, key=Winner_Dict.get)

#for candidate, vote in Winner_Dict.items():
    #if vote == max_winner:
        #print candidate


#print results
print ("Election Results")
print("----------------------")
print("Total Votes: " + str(len(votes_count)))
print("----------------------")
print("Charles Casper Stockham: " + str(Stockham_percent) + " (" + str(Stockham_count) + ")")
print("Diana DeGette: " + str(DeGette_percent) + " (" + str(DeGette_count) + ")")
print("Raymon Anthony Doane: " + str(Doane_percent) + " (" + str(Doane_count) + ")")
print("Winner: " + max_winner)


#write results to a new file
f = open("/Users/wenlirui/Downloads/PyPoll.txt", "a")
f.write("Election Results")
f.write("\n----------------------")
f.write("\nTotal Votes: " + str(len(votes_count)))
f.write("\n----------------------")
f.write("\nCharles Casper Stockham: " + str(Stockham_percent) + " (" + str(Stockham_count) + ")")
f.write("\nDiana DeGette: " + str(DeGette_percent) + " (" + str(DeGette_count) + ")")
f.write("\nRaymon Anthony Doane: " + str(Doane_percent) + " (" + str(Doane_count) + ")")
f.write("\n----------------------")
f.write("\nWinner: " + max_winner)
f.write("\n----------------------")
f.close()

