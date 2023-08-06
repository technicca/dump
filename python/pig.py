import random

MIN = 1
MAX = 6
MAX_SCORE = 100

def roll_dice():
    return random.randint(MIN, MAX)

def player_turn(player, score):
    turn_score = 0
    while True:
        choice = input(f'Player {player}, your score this turn is {turn_score}. Do you want to roll? Y or N? ').lower()
        if choice == 'y':
            roll = roll_dice()
            if roll == 1:
                print(f'You rolled a 1, you lose all points this turn, total score is {score}, your turn is over!')
                return score
            else:
                turn_score += roll
            print(f'Player {player} rolled a {roll}')
        else:
            score += turn_score
            print(f'Player {player}, total score is {score}')
            return score

def game_turn(player, players, score):
    if player > players:
        return score
    else:
        score = player_turn(player, score)
        if score >= MAX_SCORE:
            print(f'Player {player} wins with a score of {score}!')
            return score
        else:
            return game_turn(player % players + 1, players, score)

players = 0
while players < 2 or players > 4:
    players = int(input("Enter the number of players: (2-4)"))
    print("Please enter a number between 2 and 4")
    print('Total players:', players)

game_turn(1, players, 0)


# or use a list:
# scores = [0]*players
# while max(scores) < MAX_SCORE: