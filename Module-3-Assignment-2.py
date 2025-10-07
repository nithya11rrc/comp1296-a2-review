"""
Name: 
Student ID: 
Date: 
Assignment 2 
Build a code to get inputs from the user to create a Leaderboard 
and a summry
"""

# # Test data
# players = [("Sally", 95), ("Toby", 88), ("Sandeep", 10), ("Alice", 5)]

# Feature: Get input from user for name and score
players = []
while True:
    player_name = input("Enter player name (or \"done\"): ")
    if player_name.lower() == "done":
        break
    elif player_name == "":
        print("The name cannot be blank.")
        continue
    else: 
        player_score = input(f"Enter score for {player_name}: ")
        try:
            if int(player_score) >= 0:
                player = (player_name, int(player_score))
                players.append(player)
        except:
            print("Invalid score. Skipping this entry")

# Feature: Length or Number of Players
"""
Use the list of tuples 
Use the length function to get the number of players
"""
# player_count = len(players)

# Refactor as a function
def count_players(players):
    return len(players)

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

# Feature: Highest Score
"""
set hightest_score_name, highest_score from first player
for each player:
    if playe's score > highest_score:
        update highest_score_name, highest_score
update the print statement
"""
# highest_score_name, highest_score = players[0]
# for name, score in players:
#     if score > highest_score:
#         highest_score_name, highest_score = name, score

# Refactor to function
def find_highest_score(players):
    highest_score_name, highest_score = players[0]
    for name, score in players:
        if score > highest_score:
            highest_score_name, highest_score = name, score
    return highest_score_name, highest_score

# Feature: Lowest score
"""
set lowest_score_name, lowest_score from the first player
For each player:
    if the player's score < lowest_score:
        update lowest_score_name, lowest_score
Print int he summary
"""
# lowest_score_name, lowest_score = players[0]
# for name, score in players:
#     if score < lowest_score:
#         lowest_score_name, lowest_score = name, score

# Refactor to function
def find_lowest(players):
    lowest_score_name, lowest_score = players[0]
    for name, score in players:
        if score < lowest_score:
            lowest_score_name, lowest_score = name, score
    return lowest_score_name, lowest_score  

# Leaderboard 
# print("=== Leaderboard ===")
# Feature: Add a leaderboard with top 3 players
# if players: 
#     top_scores = players[:]
#     for rank in range(1, 4):
#         if not top_scores:
#             break
#         best_player, best_score = top_scores[0]
#         for player, score in top_scores[1:]:
#             if score > best_score:
#                 best_player, best_score = player, score
#         print(f"{rank}. {best_player} - {best_score}")

#         top_scores.remove((best_player, best_score))
# else:
#     print("No players to display.")

# Refactor to function
def leaderboard(players):
    if players: 
        top_scores = players[:]
        for rank in range(1, 4):
            if not top_scores:
                break
            best_player, best_score = top_scores[0]
            for player, score in top_scores[1:]:
                if score > best_score:
                    best_player, best_score = player, score
            print(f"{rank}. {best_player} - {best_score}")

            top_scores.remove((best_player, best_score))
    else:
        print("No players to display.")


# Expected Output
if players:
    player_count = count_players(players)
    avg = calculate_avg_score(players) 
    highest_score_name, highest_score = find_highest_score(players)
    lowest_score_name, lowest_score = find_lowest(players)
    print("=== Leaderboard ===")
    leaderboard(players)
    print("=== Summary ===")
    print(f"Players: {player_count}")
    print(f"Highest: {highest_score_name} - {highest_score}")
    print(f"Lowest:  {lowest_score_name} - {lowest_score}")
    print(f"Average: {avg}")
else:
    print("No players entered.")

