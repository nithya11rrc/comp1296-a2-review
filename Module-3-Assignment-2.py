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


# Expected Output
print("=== Leaderboard ===")
print(f"{None}")
print(f"{None}")
print(f"{None}")


print("=== Summary ===")
print(f"Players: {player_count}")
print(f"Highest: {None}")
print(f"Lowest:  {None}")
print(f"Average: {None}")

