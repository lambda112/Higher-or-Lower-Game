from random import choice
from game_stats import data
game_data = data

# To Do List

# Get two random people 

a = choice(game_data)
b = choice(game_data)
while a == b:
    a = choice(game_data)
    b = choice(game_data)

print(f"{a=}\n{b=}")

# Output Suitable versus message 
# Allow user to input either a or b regarding who has the higher follower count
# If statement decide if user conitues depending if they were correct or not 
# If wrong end game print who had higher
# If correct increase score, continue with correct choice, remove wrong answer for 3 turns atleast 

