from random import choice
from game_stats import data
from art import versus_art

game_data = data
score = 0 

# Get two random people 
a = choice(game_data)
b = choice(game_data)
while a == b:
    a = choice(game_data)
    b = choice(game_data)


# Output Suitable versus message 
print(f"Compare A: {a['name']} a {a['description']} from {a['country']}")
print(versus_art)
print(f"Against B: {b['name']} a {b['description']} from {b['country']}")


# Allow user to input either a or b regarding who has the higher follower count
# If statement decide if user conitues depending if they were correct or not 
# If wrong end game print who had higher
# If correct increase score, continue with correct choice, remove wrong answer for 3 turns atleast 

user_answer = input("Who has the most followers! (a or b): ").lower()
answer = "a" if a["follower_count"] > b["follower_count"] else "b" if a["follower_count"] < b["follower_count"] else "Equal"
ans_dict = {
    "a": a["follower_count"],
    "b": b["follower_count"] 
}

if answer == user_answer:
    print(f"Correct! The answer was {answer} with {ans_dict[answer]},000,000")
    score += 1

elif answer == "Equal":
    print(f"Both celebrities have the same amount of followers! {answer} with {ans_dict[answer]},000,000")
    score += 1 

else:
    print(f"Wrong! You Lose! The answer was {answer} with {ans_dict[answer]},000,000")



# Repeat Code until loser loses


