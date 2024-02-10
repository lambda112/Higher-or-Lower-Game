from random import choice
from game_stats import data
from art import versus_art
from os import system

game_data = data
score = 0


def get_celeb_data(): 
    """Return data on two random celebrities"""
    a = choice(game_data)
    b = choice(game_data)

    while a == b:
        a = choice(game_data)
        b = choice(game_data)

    return a,b




def versus_message(a,b):
    """Output Suitable versus message"""
    print(f"Compare A: {a['name']} a {a['description']} from {a['country']}")
    print(versus_art)
    print(f"Against B: {b['name']} a {b['description']} from {b['country']}")




def user_input():
    """Get user input regarding thier answer a or b"""
    while True:
        user_answer = input(f"Who has the most followers! (a or b): ").lower()

        if user_answer in ["a", "b"]:
            return user_answer
        
        else:
            print("Please enter a valid input!")



def game_logic(a,b):
    "Compares user answer against actual answer and returns false if wrong or the answer if correct"
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




def new_pair(pair,result):
    "Takes the pair of celebrites and the correct answer to return a new pair including the correct result from the previous exchange"
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
            a = ans_dict[result]
            _,b = get_celeb_data() 

            if a == b:
                continue
            else:
                return a,b



def main():
    """Repeat Code until user loses"""
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

