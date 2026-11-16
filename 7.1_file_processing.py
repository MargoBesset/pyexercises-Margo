"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - Inconsistent capitals: "ada LOVELACE" (first name lower, last name upper),
#   "grace hopper" (all lower), "GUIDO van rossum" (mixed). No line is
#   written the same way as the others.
# - Empty lines: lines 3 and 9 are blank (line 3 may contain only spaces),
#   and line 11 looks empty at the end of the file.
# - Extra spaces at the start of a line: line 4 "  alan TURING" and
#   line 7 "  linus torvalds" begin with two spaces.
# - A name with three words: "GUIDO van rossum" (line 8). "van" is a particle
#   that belongs to the family name, so "last word = last name" is not
#   obviously right here.
# - The file is not sorted by last name (Lovelace, Hopper, Turing, ...).
# - Duplicates: I looked and found none, so my program does not remove any.

# 1. In: The file names.txt, read line by line (10 or 11 lines, depending on
#    how line 11 is stored). Nothing is typed by the user. The file is opened
#    only with "r", so the original is never modified.
# 2. Process, problem by problem:
#    - Empty lines (3, 9, 11): after split(), a blank line gives an empty
#      list, so I skip it and count it.
#    - Spaces at the start of a line (4, 7): split() ignores them.
#    - Inconsistent capitals (1, 2, 8): each word is rewritten with a capital
#      first letter and lowercase for the rest, using capitalize().
#    - "van" in line 8: capitalize() would give "Van", so I keep a small list
#      of particles (van, von, de...) that stay lowercase when they are not
#      the first word. Result: "Guido van Rossum".
#    - Not sorted: sort() with a key function that returns the last word.
# 3. Out: A new file, names_clean_sorted.txt, with 8 clean names, one per
#    line, sorted by last name. The screen shows lines read, lines kept,
#    lines removed, and the first and last name of the sorted list.
# 4. How I decide which word is the last name: the last word of the cleaned
#    line. For "Guido van Rossum" that is "Rossum", so he is sorted under R,
#    between Liskov/Lovelace and Torvalds. Limit: if someone's family name is
#    really "van Rossum" or "de la Cruz" and I wanted it under V or D, this
#    rule would be wrong. I accept this limit because the file has only one
#    such case.


# Your code below

INPUT_FILE = "names.txt"
OUTPUT_FILE = "names_clean_sorted.txt"
PARTICLES = ["van", "von", "de", "der", "da", "di", "la"]


def clean_name(line):
    """Return a clean name, or None if the line is empty."""
    words = line.split()  # removes spaces at the ends and between words
    if len(words) == 0:
        return None
    fixed_words = []
    for position, word in enumerate(words):
        if position > 0 and word.lower() in PARTICLES:
            fixed_words.append(word.lower())
        else:
            fixed_words.append(word.capitalize())
    return " ".join(fixed_words)


def last_name_key(name):
    return name.split()[-1].lower()


with open(INPUT_FILE, "r", encoding="utf-8") as file:
    raw_lines = file.readlines()

clean_names = []
empty_lines = 0

for line in raw_lines:
    name = clean_name(line)
    if name is None:
        empty_lines = empty_lines + 1
    else:
        clean_names.append(name)

clean_names.sort(key=last_name_key)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    for name in clean_names:
        file.write(name + "\n")

print("Lines in", INPUT_FILE + ":", len(raw_lines))
print("Lines in", OUTPUT_FILE + ":", len(clean_names))
print("Removed as empty:", empty_lines)
print("First:", clean_names[0] if clean_names else "none")
print("Last: ", clean_names[-1] if clean_names else "none")