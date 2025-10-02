#!/usr/bin/env python3
# cooler-multiplayer-battle-of-dices-dict.py
# Same spirit as your COOLER multiplayer version, but with dictionaries + deepcopy.
# Each player dict keeps: name, email, country, wins, rolls (per-round totals).

import random
import copy

# --- Inputs (same ideas as your second code) ---

def ask_int(prompt, minimum=None, default=None):
    """Ask for an integer with optional minimum and default (if user presses ENTER)."""
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

def print_scoreboard(players):
    board = " | ".join(f"{p['name']}: {p['wins']}" for p in players)
    print("Scoreboard →", board)

print(" Welcome to Battle of Dices — COOLER Dict Edition! ")
print("-" * 60)

# --- Setup ---
num_players = ask_int("How many players? (min 2): ", minimum=2)

# Player template
player_template = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": [],   # totals per round
}

players = []
for i in range(1, num_players + 1):
    p = copy.deepcopy(player_template)
    name = input(f"Enter name for Player {i} (leave blank for 'Player {i}'): ").strip() or f"Player {i}"
    p["name"] = name
    p["email"] = input(f"Enter e-mail for {name} (optional): ").strip()
    p["country"] = input(f"Enter country for {name} (optional): ").strip()
    players.append(p)

target_wins = ask_int("First to how many round wins? (default 3): ", minimum=1, default=3)

print("\nEach round everyone rolls a D20 and a D6 — highest total wins the round.")
print("Ties for first → this round is a tie (no points).")
print("-" * 60)

# --- Game loop ---
round_no = 1
while max(p['wins'] for p in players) < target_wins:
    input(f"\nRound {round_no}: Press ENTER to roll the dice...")
    round_totals = []  # list of (player_dict, total) for this round

    # Everyone rolls
    for p in players:
        d20, d6, total = roll_d20_d6()
        p["rolls"].append(total)
        round_totals.append((p, total))
        print(f"{p['name']} rolled D20={d20}, D6={d6} → Total = {total}")

    # Decide round result (tie → no point)
    top_total = max(total for _, total in round_totals)
    leaders = [p for p, total in round_totals if total == top_total]

    if len(leaders) == 1:
        leaders[0]["wins"] += 1
        print(f" {leaders[0]['name']} wins this round with the higher total!")
    else:
        tied_names = ", ".join(p["name"] for p in leaders)
        print(f" This round is a tie between: {tied_names}!")

    print_scoreboard(players)
    round_no += 1

# --- Game over ---
rounds_played = round_no - 1
champ = max(players, key=lambda p: p["wins"])
print(f"\n🏆 {champ['name']} is the Champion of the COOLER dict edition!")
print("Total rounds played:", rounds_played)

# Final summary
print("\nFinal Scores:")
for p in players:
    print(f"  {p['name']}: {p['wins']}")

print("\nRoll history (totals by round):")
for p in players:
    print(f"  {p['name']}: {p['rolls']}")

print("\nPlayer details:")
for p in players:
    email = p['email'] or '-'
    country = p['country'] or '-'
    print(f"  {p['name']}: email={email}, country={country}")
