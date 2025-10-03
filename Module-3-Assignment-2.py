"""
Name: 
Student ID: 
Date: 
Assignment 2 
Build a code to get inputs from the user to create a Leaderboard 
and a summry
"""

# Test data
players = [("Sally", 95), ("Toby", 88), ("Sandeep", 10), ("Alice", 5)]

# Feature: Length or Number of Players
"""
Use the list of tuples 
Use the legth function to get the number of players
"""
# player_count = len(players)
# Refactor as a function
def count_players(players):
    return len(players)

player_count = count_players(players)

# Feature: Average Scores of players
"""
Initialize total = 0
For each player in players:
    Add player's score to the total
average = total/ number of players
print
"""

# total = 0
# for p in players:
#     total += p[1]
# avg = total/ player_count

# Refactor as a function
def calculate_avg_score(players):
    total = 0
    for p in players:
        total += p[1]
    return total/ player_count
avg = calculate_avg_score(players) 

# Feature: Highest Score
"""
set hightest_score_name, highest_score from first player
for each player:
    if playe's score > highest_score:
        update highest_score_name, highest_score
update the print statement
"""
highest_score_name, highest_score = players[0]
for name, score in players:
    if score > highest_score:
        highest_score_name, highest_score = name, score


# Expected Output
print("=== Leaderboard ===")
print(f"{None}")
print(f"{None}")
print(f"{None}")


print("=== Summary ===")
print(f"Players: {player_count}")
print(f"Highest: {highest_score_name} - {highest_score}")
print(f"Lowest:  {None}")
print(f"Average: {avg}")

