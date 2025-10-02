# Battle of Dices is going to be an amazing 2 player game,
# where two players face each other using only their sheer luck!
#
# BEST OF 3 (first to 2 wins) — no loops; duplicate the ROUND BLOCK if needed.

import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Keep score
player1_wins = 0
player2_wins = 0
TARGET_WINS = 2  # best of 3 => first to 2

# =============== ROUND BLOCK (copy/paste this block if needed) ===============
input("\n[Round 1] Press ENTER to roll the dice...")

player1_roll = random.randint(1, 12)  # D12
player2_roll = random.randint(1, 12)  # D12

print("Player 1 rolled:", player1_roll)
print("Player 2 rolled:", player2_roll)

if player1_roll > player2_roll:
    player1_wins += 1
    print("🔥 Player 1 takes the round!")
elif player2_roll > player1_roll:
    player2_wins += 1
    print("⚡ Player 2 takes the round!")
else:
    print("🤝 Tie! No points this round.")

print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)
# ============================================================================

# Only play Round 2 if nobody has already reached 2 wins
if player1_wins < TARGET_WINS and player2_wins < TARGET_WINS:
    # =============== ROUND BLOCK (copy/paste this block if needed) ===============
    input("\n[Round 2] Press ENTER to roll the dice...")

    player1_roll = random.randint(1, 12)  # D12
    player2_roll = random.randint(1, 12)  # D12

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    if player1_roll > player2_roll:
        player1_wins += 1
        print("🔥 Player 1 takes the round!")
    elif player2_roll > player1_roll:
        player2_wins += 1
        print("⚡ Player 2 takes the round!")
    else:
        print("🤝 Tie! No points this round.")

    print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)
    # ============================================================================

# Only play Round 3 if nobody has already reached 2 wins
if player1_wins < TARGET_WINS and player2_wins < TARGET_WINS:
    # =============== ROUND BLOCK (copy/paste this block if needed) ===============
    input("\n[Round 3] Press ENTER to roll the dice...")

    player1_roll = random.randint(1, 12)  # D12
    player2_roll = random.randint(1, 12)  # D12

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    if player1_roll > player2_roll:
        player1_wins += 1
        print("🔥 Player 1 takes the round!")
    elif player2_roll > player1_roll:
        player2_wins += 1
        print("⚡ Player 2 takes the round!")
    else:
        print("🤝 Tie! No points this round.")

    print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)
    # ============================================================================

# Final result after up to 3 rounds
print("\n===== FINAL RESULT =====")
if player1_wins >= TARGET_WINS:
    print("🏆 Player 1 wins the match (best of 3)!")
elif player2_wins >= TARGET_WINS:
    print("🏆 Player 2 wins the match (best of 3)!")
else:
    print("No winner yet (too many ties).")
    print("👉 Copy the ROUND BLOCK again at the end of this file to keep playing until someone reaches 2 wins.")

# Battle of Dices is going to be an amazing 2 player game,
# where two players face each other using only their sheer luck!
#
# BEST OF 3 (first to 2 wins) — no loops; duplicate the ROUND BLOCK if needed.

import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Keep score
player1_wins = 0
player2_wins = 0
TARGET_WINS = 2  # best of 3 => first to 2

# =============== ROUND BLOCK (copy/paste this block if needed) ===============
input("\n[Round 1] Press ENTER to roll the dice...")

player1_roll = random.randint(1, 12)  # D12
player2_roll = random.randint(1, 12)  # D12

print("Player 1 rolled:", player1_roll)
print("Player 2 rolled:", player2_roll)

if player1_roll > player2_roll:
    player1_wins += 1
    print("🔥 Player 1 takes the round!")
elif player2_roll > player1_roll:
    player2_wins += 1
    print("⚡ Player 2 takes the round!")
else:
    print("🤝 Tie! No points this round.")

print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)
# ============================================================================

# Only play Round 2 if nobody has already reached 2 wins
if player1_wins < TARGET_WINS and player2_wins < TARGET_WINS:
    # =============== ROUND BLOCK (copy/paste this block if needed) ===============
    input("\n[Round 2] Press ENTER to roll the dice...")

    player1_roll = random.randint(1, 12)  # D12
    player2_roll = random.randint(1, 12)  # D12

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    if player1_roll > player2_roll:
        player1_wins += 1
        print("🔥 Player 1 takes the round!")
    elif player2_roll > player1_roll:
        player2_wins += 1
        print("⚡ Player 2 takes the round!")
    else:
        print("🤝 Tie! No points this round.")

    print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)
    # ============================================================================

# Only play Round 3 if nobody has already reached 2 wins
if player1_wins < TARGET_WINS and player2_wins < TARGET_WINS:
    # =============== ROUND BLOCK (copy/paste this block if needed) ===============
    input("\n[Round 3] Press ENTER to roll the dice...")

    player1_roll = random.randint(1, 12)  # D12
    player2_roll = random.randint(1, 12)  # D12

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    if player1_roll > player2_roll:
        player1_wins += 1
        print("🔥 Player 1 takes the round!")
    elif player2_roll > player1_roll:
        player2_wins += 1
        print("⚡ Player 2 takes the round!")
    else:
        print("🤝 Tie! No points this round.")

    print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)
    # ============================================================================

# Final result after up to 3 rounds
print("\n===== FINAL RESULT =====")
if player1_wins >= TARGET_WINS:
    print("🏆 Player 1 wins the match (best of 3)!")
elif player2_wins >= TARGET_WINS:
    print("🏆 Player 2 wins the match (best of 3)!")
else:
    print("No winner yet (too many ties).")
    print("👉 Copy the ROUND BLOCK again at the end of this file to keep playing until someone reaches 2 wins.")
# Battle of Dices is going to be an amazing 2 player game,
# where two players face each other using only their sheer luck!
#
# BEST OF 3 (first to 2 wins) — no loops; duplicate the ROUND BLOCK if needed.

import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Keep score
player1_wins = 0
player2_wins = 0
TARGET_WINS = 2  # best of 3 => first to 2

# =============== ROUND BLOCK (copy/paste this block if needed) ===============
input("\n[Round 1] Press ENTER to roll the dice...")

player1_roll = random.randint(1, 12)  # D12
player2_roll = random.randint(1, 12)  # D12

print("Player 1 rolled:", player1_roll)
print("Player 2 rolled:", player2_roll)

if player1_roll > player2_roll:
    player1_wins += 1
    print("🔥 Player 1 takes the round!")
elif player2_roll > player1_roll:
    player2_wins += 1
    print("⚡ Player 2 takes the round!")
else:
    print("🤝 Tie! No points this round.")

print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)
# ============================================================================

# Only play Round 2 if nobody has already reached 2 wins
if player1_wins < TARGET_WINS and player2_wins < TARGET_WINS:
    # =============== ROUND BLOCK (copy/paste this block if needed) ===============
    input("\n[Round 2] Press ENTER to roll the dice...")

    player1_roll = random.randint(1, 12)  # D12
    player2_roll = random.randint(1, 12)  # D12

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    if player1_roll > player2_roll:
        player1_wins += 1
        print("🔥 Player 1 takes the round!")
    elif player2_roll > player1_roll:
        player2_wins += 1
        print("⚡ Player 2 takes the round!")
    else:
        print("🤝 Tie! No points this round.")

    print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)
    # ============================================================================

# Only play Round 3 if nobody has already reached 2 wins
if player1_wins < TARGET_WINS and player2_wins < TARGET_WINS:
    # =============== ROUND BLOCK (copy/paste this block if needed) ===============
    input("\n[Round 3] Press ENTER to roll the dice...")

    player1_roll = random.randint(1, 12)  # D12
    player2_roll = random.randint(1, 12)  # D12

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    if player1_roll > player2_roll:
        player1_wins += 1
        print("🔥 Player 1 takes the round!")
    elif player2_roll > player1_roll:
        player2_wins += 1
        print("⚡ Player 2 takes the round!")
    else:
        print("🤝 Tie! No points this round.")

    print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)
    # ============================================================================

# Final result after up to 3 rounds
print("\n===== FINAL RESULT =====")
if player1_wins >= TARGET_WINS:
    print("🏆 Player 1 wins the match (best of 3)!")
elif player2_wins >= TARGET_WINS:
    print("🏆 Player 2 wins the match (best of 3)!")
else:
    print("No winner yet (too many ties).")
    print("👉 Copy the ROUND BLOCK again at the end of this file to keep playing until someone reaches 2 wins.")
# Battle of Dices is going to be an amazing 2 player game,
# where two players face each other using only their sheer luck!
#
# BEST OF 3 (first to 2 wins) — no loops; duplicate the ROUND BLOCK if needed.

import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Keep score
player1_wins = 0
player2_wins = 0
TARGET_WINS = 2  # best of 3 => first to 2

# =============== ROUND BLOCK (copy/paste this block if needed) ===============
input("\n[Round 1] Press ENTER to roll the dice...")

player1_roll = random.randint(1, 12)  # D12
player2_roll = random.randint(1, 12)  # D12

print("Player 1 rolled:", player1_roll)
print("Player 2 rolled:", player2_roll)

if player1_roll > player2_roll:
    player1_wins += 1
    print("🔥 Player 1 takes the round!")
elif player2_roll > player1_roll:
    player2_wins += 1
    print("⚡ Player 2 takes the round!")
else:
    print("🤝 Tie! No points this round.")

print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)
# ============================================================================

# Only play Round 2 if nobody has already reached 2 wins
if player1_wins < TARGET_WINS and player2_wins < TARGET_WINS:
    # =============== ROUND BLOCK (copy/paste this block if needed) ===============
    input("\n[Round 2] Press ENTER to roll the dice...")

    player1_roll = random.randint(1, 12)  # D12
    player2_roll = random.randint(1, 12)  # D12

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    if player1_roll > player2_roll:
        player1_wins += 1
        print("🔥 Player 1 takes the round!")
    elif player2_roll > player1_roll:
        player2_wins += 1
        print("⚡ Player 2 takes the round!")
    else:
        print("🤝 Tie! No points this round.")

    print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)
    # ============================================================================

# Only play Round 3 if nobody has already reached 2 wins
if player1_wins < TARGET_WINS and player2_wins < TARGET_WINS:
    # =============== ROUND BLOCK (copy/paste this block if needed) ===============
    input("\n[Round 3] Press ENTER to roll the dice...")

    player1_roll = random.randint(1, 12)  # D12
    player2_roll = random.randint(1, 12)  # D12

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    if player1_roll > player2_roll:
        player1_wins += 1
        print("🔥 Player 1 takes the round!")
    elif player2_roll > player1_roll:
        player2_wins += 1
        print("⚡ Player 2 takes the round!")
    else:
        print("🤝 Tie! No points this round.")

    print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)
    # ============================================================================

# Final result after up to 3 rounds
print("\n===== FINAL RESULT =====")
if player1_wins >= TARGET_WINS:
    print("🏆 Player 1 wins the match (best of 3)!")
elif player2_wins >= TARGET_WINS:
    print("🏆 Player 2 wins the match (best of 3)!")
else:
    print("No winner yet (too many ties).")
    print("👉 Copy the ROUND BLOCK again at the end of this file to keep playing until someone reaches 2 wins.")
# Battle of Dices is going to be an amazing 2 player game,
# where two players face each other using only their sheer luck!
#
# BEST OF 3 (first to 2 wins) — no loops; duplicate the ROUND BLOCK if needed.

import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Keep score
player1_wins = 0
player2_wins = 0
TARGET_WINS = 2  # best of 3 => first to 2

# =============== ROUND BLOCK (copy/paste this block if needed) ===============
input("\n[Round 1] Press ENTER to roll the dice...")

player1_roll = random.randint(1, 12)  # D12
player2_roll = random.randint(1, 12)  # D12

print("Player 1 rolled:", player1_roll)
print("Player 2 rolled:", player2_roll)

if player1_roll > player2_roll:
    player1_wins += 1
    print("🔥 Player 1 takes the round!")
elif player2_roll > player1_roll:
    player2_wins += 1
    print("⚡ Player 2 takes the round!")
else:
    print("🤝 Tie! No points this round.")

print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)
# ============================================================================

# Only play Round 2 if nobody has already reached 2 wins
if player1_wins < TARGET_WINS and player2_wins < TARGET_WINS:
    # =============== ROUND BLOCK (copy/paste this block if needed) ===============
    input("\n[Round 2] Press ENTER to roll the dice...")

    player1_roll = random.randint(1, 12)  # D12
    player2_roll = random.randint(1, 12)  # D12

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    if player1_roll > player2_roll:
        player1_wins += 1
        print("🔥 Player 1 takes the round!")
    elif player2_roll > player1_roll:
        player2_wins += 1
        print("⚡ Player 2 takes the round!")
    else:
        print("🤝 Tie! No points this round.")

    print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)
    # ============================================================================

# Only play Round 3 if nobody has already reached 2 wins
if player1_wins < TARGET_WINS and player2_wins < TARGET_WINS:
    # =============== ROUND BLOCK (copy/paste this block if needed) ===============
    input("\n[Round 3] Press ENTER to roll the dice...")

    player1_roll = random.randint(1, 12)  # D12
    player2_roll = random.randint(1, 12)  # D12

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    if player1_roll > player2_roll:
        player1_wins += 1
        print("🔥 Player 1 takes the round!")
    elif player2_roll > player1_roll:
        player2_wins += 1
        print("⚡ Player 2 takes the round!")
    else:
        print("🤝 Tie! No points this round.")

    print("Score => Player 1:", player1_wins, "| Player 2:", player2_wins)
    # ============================================================================

# Final result after up to 3 rounds
print("\n===== FINAL RESULT =====")
if player1_wins >= TARGET_WINS:
    print("🏆 Player 1 wins the match (best of 3)!")
elif player2_wins >= TARGET_WINS:
    print("🏆 Player 2 wins the match (best of 3)!")
else:
    print("No winner yet (too many ties).")
    print("👉 Copy the ROUND BLOCK again at the end of this file to keep playing until someone reaches 2 wins.")
