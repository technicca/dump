# This code simulates a game of Pig, a simple dice game, playable by 2-4 players.
# The game consists of players taking turns to roll a dice and accumulate points.
# Rolling a 1 results in a loss of points for that turn, while other rolls add to the player's turn score.
# The first player to reach a total score of 100 or more wins the game.
import random

MIN = 1
MAX = 6
MAX_SCORE = 100

def roll_dice():
    # This function simulates rolling a six-sided dice by generating a random number between MIN (1) and MAX (6).
    return random.randint(MIN, MAX)

def player_turn(player, score):
    # This function simulates a single player's turn in the game of Pig.
    # During a turn, a player can roll the dice multiple times to accumulate points.
    # Rolling a 1 ends the player's turn and all points for that turn are lost.
    # The player can choose to hold and add the turn's score to their total score at any point.
    # The player's total score is returned at the end of the turn.
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
    # This function manages the sequence of turns in the game, iterating through each player.
    # It calls player_turn() to simulate each individual turn.
    # When a player's score reaches or exceeds MAX_SCORE (100), they win, and the game ends.
    # The function uses recursion to cycle through the players' turns.
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