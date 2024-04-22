import random

def run_experiment(stake, goal, bet):
    wins = 0
    count = 0

    while stake > 0 and stake != goal:
        if random.randint(0,1) == 1:  
            stake += bet
            wins += 1
        else:
            stake -= bet   
        count+=1 

    if stake >=goal:
        print("You Won")
    else:
        print("You lose")

    avg= wins / count
    win_per = (wins / count) * 100

    print(f"Average number of wins: {avg}")
    print(f"Percentage of wins: {win_per}")
    print(f"Percentage of losses: {100 - win_per}")


if __name__ == "__main__":
    try:
        stake = int(input("Enter the stake amount: "))
        goal = int(input("Enter the goal amount: "))
        bet = int(input("Enter the bet : "))
        run_experiment(stake, goal, bet)
    except ValueError:
        print("Please enter valid integer values")
