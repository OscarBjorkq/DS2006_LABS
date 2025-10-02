# battle-of-dices-better.py 
import random

print("🎲 Welcome to Battle of Dices! 🎲")

player1_wins = 0
player2_wins = 0
round_no = 1  # count rounds

while player1_wins < 3 and player2_wins < 3:
    input(f"\nRound {round_no}: Press ENTER to roll the dice...")
    p1 = random.randint(1, 6)
    p2 = random.randint(1, 6)

    print("Player 1 rolled:", p1)
    print("Player 2 rolled:", p2)

    if p1 > p2:
        player1_wins += 1
        print("Player 1 wins this round!")
    elif p2 > p1:
        player2_wins += 1
        print("Player 2 wins this round!")
    else:
        print("This round is a tie!")

    print("Score: Player 1", player1_wins, "-", player2_wins, "Player 2")
    round_no += 1


rounds_played = round_no - 1
if player1_wins == 3:
    print("🏆 Player 1 is the Champion!")
else:
    print("🏆 Player 2 is the Champion!")
print("Total rounds played:", rounds_played)
