import random

def ask_int(prompt, minimum=None, default=None):
    """Ask for an integer with optional minimum and default (if user just presses ENTER)."""
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            return default
        try:
            val = int(raw)
            if minimum is not None and val < minimum:
                print(f"Please enter a number >= {minimum}.")
                continue
            return val
        except ValueError:
            print("Please enter a valid integer.")

print("🎲 Welcome to Multiplayer Battle of Dices — Lecture 06 Edition!")

# ------------------------------
# Get number of players and their names (Lecture 06)
# ------------------------------
num_players = ask_int("How many players? (min 2): ", minimum=2)

players = []
for i in range(1, num_players + 1):
    name = input(f"Enter name for Player {i} (leave blank for 'Player {i}'): ").strip()
    if not name:
        name = f"Player {i}"
    players.append(name)

# ------------------------------
# Game parameters (configurable)
# ------------------------------
target_wins = ask_int("Target wins to become Champion? (default 3): ", minimum=1, default=3)

# ------------------------------
# Initialize scores (Lecture 06)
# ------------------------------
scores = [0 for _ in range(num_players)]

# ------------------------------
# Initialize per-player roll history (nested lists, Lecture 06)
# ------------------------------
roll_history = [[] for _ in range(num_players)]

print("\nRules: Each round, everyone rolls 1d20 + 1d6. Highest total wins the round.")
print("Ties for first = no point this round (simple tie policy).\n")

round_no = 1
while max(scores) < target_wins:
    input(f"Round {round_no}: press ENTER to roll...")
    round_totals = []  # totals for each player in player index order

    # Each player rolls 1d20 + 1d6
    for idx, name in enumerate(players):
        d20 = random.randint(1, 20)
        d6 = random.randint(1, 6)
        total = d20 + d6
        round_totals.append(total)
        roll_history[idx].append(total)
        print(f"  {name:>12} rolled D20={d20:2d}, D6={d6:2d}  → Total = {total:2d}")

    # ------------------------------
    # Check whether there were winning player(s) (Lecture 06)
    # ------------------------------
    top = max(round_totals)
    winners = [i for i, t in enumerate(round_totals) if t == top]

    if len(winners) == 1:
        w = winners[0]
        scores[w] += 1
        print(f"→ {players[w]} wins the round with {top}!")
    else:
        tied_names = ", ".join(players[i] for i in winners)
        print(f"→ Tie for first between: {tied_names}. No points awarded.")

    # Scoreboard
    score_line = " | ".join(f"{name}: {scores[i]}" for i, name in enumerate(players))
    print("Scoreboard →", score_line)
    round_no += 1
    print("-" * 60)

# ------------------------------
# Print champion and a compact summary (Lecture 06)
# ------------------------------
champ_idx = scores.index(max(scores))
print(f"\n🏆 Champion: {players[champ_idx]} with {scores[champ_idx]} wins!")

print("\nFinal Scores:")
for i, name in enumerate(players):
    print(f"  {name}: {scores[i]}")

print("\nRoll history per player (totals by round):")
for i, name in enumerate(players):
    print(f"  {name}: {roll_history[i]}")

print("\nThanks for playing!")
