# Name: Margo Besset
# Group: C
#
# FEATURE CHOSEN: (a) Streak bonus.
# Why: It is the simplest one to follow in the history list, and it gives the
# player a reason to take the safe, reputation-gaining options.
#
# THE FOUR QUESTIONS :
#
# 1. What goes in? : separator, columns, what each holds, how the numbers are written, and how you find the impact of option B.
# 2. What happens?n: the steps of one day, in order, one line each.
# 3. What comes out? : what the player sees at the end + what one line of results.csv looks like.
# 4. What could go wrong? : for example a missing file, a wrong answer typed by the player, a bad number in the file, a gauge going below zero.

# I need csv to read and write files, random to shuffle the days, and date to stamp each game in results.csv.
import csv
import random
from datetime import date

# Settings in one place, so I can change a rule without searching the code.
SCENARIO_FILE = "scenarios_C.csv"
RESULTS_FILE = "results.csv"
DAYS = 10
START_BUDGET = 10000
START_REPUTATION = 50
MAX_REPUTATION = 100
STREAK_LENGTH = 3
STREAK_BONUS = 500
LETTERS = ("A", "B", "C")

# Turns the text of the file ('+15 pts', '-800 EUR') into a real number I can add.
def parse_number(text):
    """Turn text like '+15 pts' or '-800 EUR' into an int (15, -800)."""
    # split() cuts off the unit; int() understands the + and - signs
    return int(text.strip().split()[0])

# Reads my scenario file and builds the list of days.
# Each option becomes a tuple, and a broken line is skipped instead of crashing.
def load_scenarios(filename):
    """Read the CSV file and return a list of (event, [3 option tuples]).

    Each option tuple is (text, budget_change, reputation_change, feedback).
    Columns in the file: Event, Day, Decision 1-3, Reputation 1-3,
    Budget 1-3, Outcome 1-3.
    """
    # the list of days I will fill
    scenarios = []
    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  # skip the header line
            for row in reader:
                try:
                    options = []
                    # build the three options A, B, C from their columns
                    for i in range(3):
                        text = row[2 + i]
                        reputation = parse_number(row[5 + i])
                        budget = parse_number(row[8 + i])
                        feedback = row[11 + i]
                        options.append((text, budget, reputation, feedback))
                    scenarios.append((row[0], options))
                    # missing column or a number I cannot read: skip this row
                except (IndexError, ValueError):
                    pass  # a broken line is skipped, the game goes on
    # the file is not in the folder: tell the player, do not crash
    except FileNotFoundError:
        print("Cannot find", filename, "- put it in the same folder as the game.")
    return scenarios

# Asks for the player's name and asks again if they type nothing.
def ask_name():
    """Ask the player's name until it is not empty."""
    name = input("What is your name, new marketing manager? ").strip()
    while name == "":
        name = input("Please type your name: ").strip()
    return name

# Asks for A, B or C and repeats until the answer is valid (a, b, c are fine too).
# Returns 0, 1 or 2 so I can use it as a position in the options list.
def ask_choice():
    """Ask for A, B or C until the answer is valid. Return the index 0, 1 or 2."""
    answer = input("Your choice (A, B or C): ").strip().upper()
    while answer not in LETTERS:
        answer = input("Please type A, B or C: ").strip().upper()
    return LETTERS.index(answer)

# Shows one day: the day number, the two gauges, the situation and the options.
def show_day(day, budget, reputation, event, options):
    """Print the header, the situation and the three options of one day."""
    print()
    print("--- Day", day, "---")
    print("[Budget:", budget, "EUR | Reputation:", str(reputation) + "/100]")
    print(event)
    for letter, option in zip(LETTERS, options):
        print(" " + letter + ":", option[0])

# Applies the chosen option to the two gauges and returns both new values as a tuple.
# Reputation can never go above 100.
def apply_choice(budget, reputation, option):
    """Apply an option to the gauges and return the new (budget, reputation)."""
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = min(reputation + reputation_change, MAX_REPUTATION)  # cap at 100
    return budget, reputation

# Gives the final title from the score (only used if the player survives).
def get_title(score):
    """Return the final title for a score (only used when the player survives)."""
    if score < 95:
        return "Eternal Intern"
    elif score < 120:
        return "Growth Hacker"
    elif score < 140:
        return "CMO Material"
    else:
        return "Viral Legend"

# Finds the best and the worst move in the history list.
# Tuples are compared from the first element, so the reputation change decides.
def best_and_worst(history):
    """Return (best_move, worst_move) from the history.

    A history entry is (reputation_change, day, option_text), so Python
    compares the reputation change first: max() and min() do the job.
    """
    return max(history), min(history)

# Writes a number with its sign (+20 or -10) for the messages.
def format_change(value):
    """Return a number with its sign, like +20 or -10."""
    return "{:+d}".format(value)

# Adds one line to results.csv (and the header line if the file is new).
# If the file cannot be written, the game shows a message and keeps going.
def save_result(name, budget, reputation, title):
    """Append one line to results.csv (and write the header the first time)."""
    try:
        try:
            with open(RESULTS_FILE, newline="", encoding="utf-8") as f:
                is_new = f.read(1) == ""
        except FileNotFoundError:
            is_new = True
        with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if is_new:
                writer.writerow(["name", "budget", "reputation", "title", "date"])
            writer.writerow([name, budget, reputation, title, date.today().isoformat()])
        print("Saved in", RESULTS_FILE)
    except OSError:
        print("Could not write", RESULTS_FILE, "- close it if it is open elsewhere.")

# The whole game: setup, 10 days, then the final result.
def play():
    """Play one full game."""
    print("=== SURVIVE THE QUARTER: Croissant Rocket ===")
    name = ask_name()

    scenarios = load_scenarios(SCENARIO_FILE)
    if len(scenarios) < DAYS:
        print("Not enough scenarios to play", DAYS, "days. Check", SCENARIO_FILE)
        return
    random.shuffle(scenarios)

    budget = START_BUDGET
    reputation = START_REPUTATION
    history = []          # one tuple per day: (reputation_change, day, option_text)
    streak = 0            # reputation gains in a row (feature a)
    fired_reason = ""

   # --- the 10 days ---
    for day in range(1, DAYS + 1):
        # take the next shuffled scenario and show it
        event, options = scenarios[day - 1]
        show_day(day, budget, reputation, event, options)

 # ask the player, apply the choice, remember it in the history
        choice = options[ask_choice()]
        budget, reputation = apply_choice(budget, reputation, choice)
        history.append((choice[2], day, choice[0]))

 # show the feedback line and what changed
        print(choice[3])
        print("Budget", format_change(choice[1]), "EUR, Reputation", format_change(choice[2]))

        # Feature a (streak bonus): count reputation gains in a row,
        # three in a row give 500 EUR and the counter starts again.
        if choice[2] > 0:
            streak += 1
        else:
            streak = 0
        if streak == STREAK_LENGTH:
            budget += STREAK_BONUS
            streak = 0
            print("Streak! Three reputation gains in a row: +" + str(STREAK_BONUS) + " EUR")

        # Game over check: if a gauge is 0 or less, stop the loop at once.
        if budget <= 0:
            fired_reason = "the budget hit zero"
            break
        if reputation <= 0:
            fired_reason = "your reputation hit zero"
            break

# --- the final result: fired, or survived with a score and a title ---
    print()
    print("=" * 30)
    if fired_reason:
        title = "Fired"
        print("You are FIRED: " + fired_reason + ".")
        print("Budget left:", budget, "EUR, reputation:", str(reputation) + "/100")
    else:
        print("Quarter survived!")
        print("Budget left:", budget, "EUR, reputation:", str(reputation) + "/100")
        score = reputation + budget // 200
        title = get_title(score)
        print("Final score:", score)
        print(name + ", your title:", title)

# best and worst move of the game
    best, worst = best_and_worst(history)
    print('Best move: day {}, "{}" ({})'.format(best[1], best[2], format_change(best[0])))
    print('Worst move: day {}, "{}" ({})'.format(worst[1], worst[2], format_change(worst[0])))

# one line in results.csv
    save_result(name, budget, reputation, title)

# Start the game. If the player quits with Ctrl+C or Ctrl+D, end politely.
try:
    play()
except (EOFError, KeyboardInterrupt):
    print("\nGame stopped. See you next quarter!")