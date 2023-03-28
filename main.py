import random

def main():
    num_of_players = input("Please provide num of players (min 2 players) ").strip()
    try:
        num_of_players = int(num_of_players)
    except:
        print("Please make sure you provide a number!")
        return
    player_answers = {}
    random_num = random.randint(1,20)
    i = 1
    print(num_of_players)
    while num_of_players > 0:
        name = input(f"Player {i}, please enter your name ")
        answer = provide_answer(name)
        player_answers[name] = answer
        i+=1
        num_of_players-=1
    closest = None
    for key, value in player_answers.items():
        if not closest:
            closest = [key, abs(random_num - value)]
        else:
            if closest[1] > abs(random_num - value):
                closest = [key, value]
    print(f"{closest[0]} wins as his number: {closest[1]} is the closest to the random num: {random_num}")
    

def provide_answer(name: str):
    correct_type = False
    while not correct_type:
        answer = input(f"{name}, please guess the number ")
        try:
            answer = int(answer)
            correct_type = True
        except:
             print("Please make sure you provide a number!")
    return answer


main()