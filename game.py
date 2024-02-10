from random import choice
from game_stats import data
from art import versus_art
game_data = data


# Get two random people 
a = choice(game_data)
b = choice(game_data)
while a == b:
    a = choice(game_data)
    b = choice(game_data)


# Output Suitable versus message 
print(f"Compare A: {a['name']} a {a['description']} from {a['country']}")
print(versus_art)
print(f"Against B: {b['name']} a {b['description']} from {a['country']}")

# Allow user to input either a or b regarding who has the higher follower count
# If statement decide if user conitues depending if they were correct or not 
# If wrong end game print who had higher
# If correct increase score, continue with correct choice, remove wrong answer for 3 turns atleast 

