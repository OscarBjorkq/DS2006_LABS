# battle-of-dices-not-rigged.py
import random

print("Welcome to Battle of Dices! (Not Rigged)")

player1_wins = 0
player2_wins = 0
round_no = 1  # count rounds

# Nya listor för att lagra alla slag
player1_rolls = []
player2_rolls = []

while player1_wins < 3 and player2_wins < 3:
    input(f"\nRound {round_no}: Press ENTER to roll the dice...")

    # Slå tärning och spara i listorna
    p1 = random.randint(1, 6)   # du kan byta till D12, D20 etc. om du vill
    p2 = random.randint(1, 6)

    player1_rolls.append(p1)
    player2_rolls.append(p2)

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
    print("Player 1 is the Champion!")
else:
    print("Player 2 is the Champion!")
print("Total rounds played:", rounds_played)

# ===== Game Summary using the lists =====
print("\n===== GAME SUMMARY =====")
print("Player 1 rolls:", player1_rolls)
print("Player 2 rolls:", player2_rolls)

# ===== GAME SUMMARY (Task 4) =====
print("\n===== GAME SUMMARY =====")

# Information om vilken typ av tärning som användes (byt text om du använde annan)
dice_type = "D6"

# Antal rundor som faktiskt spelades
rounds = list(range(1, rounds_played + 1))

# Bygg header
header = "| Round    | " + " | ".join(str(r).rjust(3) for r in rounds) + " |"
row_p1 = "| Player 1 | " + " | ".join(str(v).rjust(3) for v in player1_rolls) + " |"
row_p2 = "| Player 2 | " + " | ".join(str(v).rjust(3) for v in player2_rolls) + " |"

# Separator
sep = "-" * len(header)

# Skriv ut tabellen
print(f"Dice used: {dice_type}")
print(sep)
print(header)
print(sep)
print(row_p1)
print(sep)
print(row_p2)
print(sep)

# ===== SAVE SUMMARY TO FILE (Task 5) =====
filename = input("\nEnter the filename to save the game summary (e.g., summary.txt): ")

with open(filename, "w") as f:
    f.write("===== GAME SUMMARY =====\n")
    f.write(f"Dice used: {dice_type}\n")
    f.write(sep + "\n")
    f.write(header + "\n")
    f.write(sep + "\n")
    f.write(row_p1 + "\n")
    f.write(sep + "\n")
    f.write(row_p2 + "\n")
    f.write(sep + "\n")

print(f"\nGame summary saved to '{filename}'.")
