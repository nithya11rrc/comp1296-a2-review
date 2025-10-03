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

total = 0
for p in players:
    total += p[1]
avg = total/ player_count

# Expected Output
print("=== Leaderboard ===")
print(f"{None}")
print(f"{None}")
print(f"{None}")


print("=== Summary ===")
print(f"Players: {player_count}")
print(f"Highest: {None}")
print(f"Lowest:  {None}")
print(f"Average: {avg}")

