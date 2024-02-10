from random import choice
from game_stats import data
from art import versus_art
from os import system

game_data = data
score = 0


# Get two random people
def get_celeb_data(): 
    a = choice(game_data)
    b = choice(game_data)

    while a == b:
        a = choice(game_data)
        b = choice(game_data)

    return a,b



# Output Suitable versus message 
def versus_message(a,b):
    print(f"Compare A: {a['name']} a {a['description']} from {a['country']}")
    print(versus_art)
    print(f"Against B: {b['name']} a {b['description']} from {b['country']}")



# Get User Input
def user_input():
    while True:
        user_answer = input(f"Who has the most followers! (a or b): ").lower()

        if user_answer in ["a", "b"]:
            return user_answer
        
        else:
            print("Please enter a valid input!")



# Allow user to input either a or b regarding who has the higher follower count
def game_logic(a,b):

    global score
    user_answer = user_input()
    answer = "a" if a["follower_count"] > b["follower_count"] else "b" if a["follower_count"] < b["follower_count"] else "Equal"

    if answer == user_answer:
        system("cls")
        score += 1
        print(f"Correct! Current Score: {score}")

    else:
        print(f"\nWrong! You Lose!")
        print(f"Final Score: {score}")
        return False
    
    return answer



# Get new pair of celebrities after correct guess
def new_pair(pair,result):

    ans_dict = {
        "a": pair[0],
        "b": pair[1] 
    }

    while True:

        if result == "a":
            a = ans_dict[result]
            _,b = get_celeb_data() 

            if a == b:
                continue
            else:
                return a,b

        else:
            b = ans_dict[result]
            a,_ = get_celeb_data() 

            if a == b:
                continue
            else:
                return a,b



# Repeat Code until loser loses
def main():
    cont = True
    celeb_pair = get_celeb_data()

    while cont == True:
        versus_message(*celeb_pair)
        result = game_logic(*celeb_pair)
        
        if result == False:
            print("Well Done!")
            cont = False

        else:
            celeb_pair = new_pair(celeb_pair,result)


main()

