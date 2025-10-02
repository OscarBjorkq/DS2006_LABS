#battle-of-dices-bad-not-rigged.py
# BEST OF 3 (first to 2 wins) — no loops
# Task 1: Use separate variables for each player's roll in each round (D6).

import random

print("🎲 Welcome to Battle of Dices! (Not Rigged) 🎲")

# Score
player1_wins = 0
player2_wins = 0
TARGET_WINS = 2  # best of 3

# ========================== ROUND 1 (No loops) ==========================
input("\n[Round 1] Press ENTER to roll the dice...")

player1__round1_roll = random.randint(1, 6)  # D6
player2__round1_roll = random.randint(1, 6)  # D6

print("Player 1 rolled:", player1__round1_roll)
print("Player 2 rolled:", player2__round1_roll)

if player1__round1_roll > player2__round1_roll:
    player1_wins += 1
    print("🔥 Player 1 takes Round 1!")
elif player2__round1_roll > player1__round1_roll:
    player2_wins += 1
    print("⚡ Player 2 takes Round 1!")
else:
    print("🤝 Round 1 is a tie — no points.")

print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)

# ========================== ROUND 2 (only if needed) ==========================
if player1_wins < TARGET_WINS and player2_wins < TARGET_WINS:
    input("\n[Round 2] Press ENTER to roll the dice...")

    player1__round2_roll = random.randint(1, 6)  # D6
    player2__round2_roll = random.randint(1, 6)  # D6

    print("Player 1 rolled:", player1__round2_roll)
    print("Player 2 rolled:", player2__round2_roll)

    if player1__round2_roll > player2__round2_roll:
        player1_wins += 1
        print("🔥 Player 1 takes Round 2!")
    elif player2__round2_roll > player1__round2_roll:
        player2_wins += 1
        print("⚡ Player 2 takes Round 2!")
    else:
        print("🤝 Round 2 is a tie — no points.")

    print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)

# ========================== ROUND 3 (only if needed) ==========================
if player1_wins < TARGET_WINS and player2_wins < TARGET_WINS:
    input("\n[Round 3] Press ENTER to roll the dice...")

    player1__round3_roll = random.randint(1, 6)  # D6
    player2__round3_roll = random.randint(1, 6)  # D6

    print("Player 1 rolled:", player1__round3_roll)
    print("Player 2 rolled:", player2__round3_roll)

    if player1__round3_roll > player2__round3_roll:
        player1_wins += 1
        print("🔥 Player 1 takes Round 3!")
    elif player2__round3_roll > player1__round3_roll:
        player2_wins += 1
        print("⚡ Player 2 takes Round 3!")
    else:
        print("🤝 Round 3 is a tie — no points.")

    print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)

# ===== GAME SUMMARY (Task 2) =====
print("\n===== GAME SUMMARY =====")

# Samla ihop spelade rundor utan loopar (lägg till fler rader om du gör fler rundor)
round_labels = []
p1_vals = []
p2_vals = []

# Round 1 (alltid finns)
round_labels.append("1")
p1_vals.append(player1__round1_roll)
p2_vals.append(player2__round1_roll)

# Round 2 (finns bara om den kördes)
if 'player1__round2_roll' in globals():
    round_labels.append("2")
    p1_vals.append(player1__round2_roll)
    p2_vals.append(player2__round2_roll)

# Round 3 (finns bara om den kördes)
if 'player1__round3_roll' in globals():
    round_labels.append("3")
    p1_vals.append(player1__round3_roll)
    p2_vals.append(player2__round3_roll)


col_width = 3  
header = "| Round    | " + " | ".join(label.rjust(col_width) for label in round_labels) + " |"
row_p1 = "| Player 1 | " + " | ".join(str(v).rjust(col_width) for v in p1_vals) + " |"
row_p2 = "| Player 2 | " + " | ".join(str(v).rjust(col_width) for v in p2_vals) + " |"

# separator-linje
sep_len = len(header)
sep = "-" * sep_len

print(sep)
print(header)
print(sep)
print(row_p1)
print(sep)
print(row_p2)
print(sep)

# ========================== FINAL RESULT ==========================
print("\n===== FINAL RESULT =====")
if player1_wins >= TARGET_WINS:
    print("🏆 Player 1 wins the match (best of 3)!")
elif player2_wins >= TARGET_WINS:
    print("🏆 Player 2 wins the match (best of 3)!")
else:
    print("No winner yet (too many ties).")
    print("👉 Copy a new ROUND block (Round 4) at the end to continue until someone reaches 2 wins.") 


