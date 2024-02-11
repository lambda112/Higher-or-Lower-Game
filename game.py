import random
import os
from game_stats import data
from art import versus_art


game_data = data
def get_celeb_data(a = None): 
    """Return data on two random celebrities"""
    if a:
        b = random.choice(game_data)
        while a and a == b:
            b = random.choice(game_data)

        return a,b

    return random.sample(game_data, k=2)



def versus_message(celeb_a:list[dict], celeb_b:list[dict]):
    """Output Suitable versus message"""
    print(f"Compare A: {celeb_a['name']} a {celeb_a['description']} from {celeb_a['country']}")
    print(versus_art)
    print(f"Against B: {celeb_b['name']} a {celeb_b['description']} from {celeb_b['country']}")



def user_input() -> str:
    """Get user input regarding thier answer a or b"""
    while True:
        user_answer = input(f"Who has the most followers! (a or b): ").lower()
        if user_answer in ["a", "b"]:
            return user_answer
        else:
            print("Please enter a valid input!")



def game_logic(a: list[dict], b:list[dict]) -> bool | str:
    "Compares user answer against actual answer and returns false if wrong or the answer if correct"
    user_answer = user_input()
    answer = "a" if a["follower_count"] > b["follower_count"] else "b" if a["follower_count"] < b["follower_count"] else "Equal"

    if answer == user_answer:
        os.system("cls")

    else:
        print(f"\nWrong! You Lose!")
        return False
    
    return answer, True



def new_pair(pair: list[dict],result:str) -> dict:
    "Takes the pair of celebrites and the correct answer to return a new pair including the correct result from the previous exchange"
    ans_dict = {
        "a": pair[0],
        "b": pair[1] 
    }

    celeb_a, celeb_b = get_celeb_data(ans_dict[result])
    return celeb_a, celeb_b



def main():
    """Repeat Code until user loses"""
    cont = True
    score = 0
    celeb_pair = get_celeb_data()

    while cont == True:
        versus_message(*celeb_pair)
        result = game_logic(*celeb_pair)

        if result == False:
            print("Well Done!")
            print(f"Final Score: {score}")
            cont = False
        else:
            celeb_pair = new_pair(celeb_pair,result[0])
            score += 1
            print(f"Correct! Current Score: {score}")


main()

