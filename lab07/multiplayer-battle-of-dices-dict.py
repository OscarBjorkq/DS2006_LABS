# multiplayer-battle-of-dices-dict.py
# Enkel Lecture 07-version med dictionaries + deepcopy.
# Varje spelare: name, email, country, wins, rolls.

import random
import copy

def ask_int_min(prompt, minimum):
    """Fråga efter ett heltal >= minimum."""
    while True:
        s = input(prompt).strip()
        try:
            n = int(s)
            if n < minimum:
                print(f"Please enter a number >= {minimum}.")
                continue
            return n
        except ValueError:
            print("Please enter a whole number, e.g. 3.")

print("🎲 Welcome to Multiplayer Battle of Dices — Dict Edition!")

# ----- Player template (dict) -----
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []   # totals per round
}

# ----- Setup: antal spelare + info -----
number_of_players = ask_int_min("How many players? (min 2): ", 2)
players = []

# For loop to obtain the player names + extra info:
for i in range(number_of_players):
    # Make a deep copy of the template for this player:
    player = copy.deepcopy(player_info)

    player["name"]    = input(f"What is the name of Player {i+1}? ").strip() or f"Player {i+1}"
    player["email"]   = input(f"What is the e-mail of Player {i+1}? ").strip()
    player["country"] = input(f"What is the country of Player {i+1}? ").strip()

    players.append(player)

# Mål: först till X vinster
target_wins = ask_int_min("First to how many wins? (min 1): ", 1)

print("\nRule: Everyone rolls 1d20 + 1d6. Highest total wins the round.")
print("Tie for first → no point.\n")

# ----- Game loop -----
round_no = 1
while max(p["wins"] for p in players) < target_wins:
    input(f"Round {round_no}: press ENTER to roll...")
    round_results = []

    for p in players:
        d20 = random.randint(1, 20)
        d6  = random.randint(1, 6)
        total = d20 + d6
        p["rolls"].append(total)
        round_results.append((p, total))
        print(f"  {p['name']} rolled D20={d20}, D6={d6} → Total = {total}")

    # Vem/vilka vann rundan?
    top = max(t for _, t in round_results)
    leaders = [p for p, t in round_results if t == top]

    if len(leaders) == 1:
        leaders[0]["wins"] += 1
        print(f"→ {leaders[0]['name']} wins the round with {top}!")
    else:
        names = ", ".join(p["name"] for p in leaders)
        print(f"→ Tie for first between: {names}. No points awarded.")

    # Scoreboard
    print("Scoreboard → " + " | ".join(f"{p['name']}: {p['wins']}" for p in players))
    print("-" * 50)
    round_no += 1

# ----- Resultat -----
champ = max(players, key=lambda p: p["wins"])
print(f"\n🏆 Champion: {champ['name']} ({champ['wins']} wins)")

print("\nFinal Scores:")
for p in players:
    print(f"  {p['name']}: {p['wins']} (email: {p['email'] or '-'}, country: {p['country'] or '-'})")

print("\nRoll history (totals by round):")
for p in players:
    print(f"  {p['name']}: {p['rolls']}")
