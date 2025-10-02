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

def roll_d20_d6():
    """Roll 1d20 and 1d6 and return (d20, d6, total)."""
    d20 = random.randint(1, 20)
    d6 = random.randint(1, 6)
    return d20, d6, d20 + d6

def print_scoreboard(players, scores):
    board = " | ".join(f"{name}: {scores[i]}" for i, name in enumerate(players))
    print("Scoreboard →", board)

print(" Welcome to Battle of Dices — COOLER Multiplayer Edition! ")
print("-" * 60)

# --- Setup (same spirit as 'cooler' 2-player version, generalized) ---
num_players = ask_int("How many players? (min 2): ", minimum=2)

players = []
for i in range(1, num_players + 1):
    name = input(f"Enter name for Player {i} (leave blank for 'Player {i}'): ").strip()
    if not name:
        name = f"Player {i}"
    players.append(name)

target_wins = ask_int("First to how many round wins? (default 3): ", minimum=1, default=3)

scores = [0] * num_players
roll_history = [[] for _ in range(num_players)]  # keep totals per round, per player

print("\nEach round everyone rolls a D20 and a D6 — highest total wins the round.")
print("Ties for first → this round is a tie (no points).")
print("-" * 60)

round_no = 1
while max(scores) < target_wins:
    input(f"\nRound {round_no}: Press ENTER to roll the dice...")
    round_totals = []

    # --- Everyone rolls (keep the COOLER per-player printouts) ---
    for idx, name in enumerate(players):
        d20, d6, total = roll_d20_d6()
        roll_history[idx].append(total)
        round_totals.append(total)
        print(f"{name} rolled D20={d20}, D6={d6} → Total = {total}")

    # --- Decide round result (same rule as original: tie → no point) ---
    top = max(round_totals)
    leaders = [i for i, t in enumerate(round_totals) if t == top]

    if len(leaders) == 1:
        w = leaders[0]
        scores[w] += 1
        print(f" {players[w]} wins this round with the higher total!")
    else:
        print(" This round is a tie!")

    print_scoreboard(players, scores)
    round_no += 1

# --- Game over ---
rounds_played = round_no - 1
champ_idx = scores.index(max(scores))
print(f"\n🏆 {players[champ_idx]} is the Champion of the COOLER multiplayer edition!")
print("Total rounds played:", rounds_played)

# Optional: print final summary and per-player roll history
print("\nFinal Scores:")
for i, name in enumerate(players):
    print(f"  {name}: {scores[i]}")

print("\nRoll history (totals by round):")
for i, name in enumerate(players):
    print(f"  {name}: {roll_history[i]}")
