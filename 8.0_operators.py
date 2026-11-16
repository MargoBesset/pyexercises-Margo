"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Nothing typed by the user. Two values written in the code:
#    first = "Python" and second = "python" (same word, different capital).
# 2. Process: The program applies the six comparison operators to the two
#    values (==, !=, <, >, <=, >=). Then it takes two of those results,
#    called p and q, and combines them with and, or, not.
#    p = (first < second), q = (first == second).
# 3. Out: A table with one row per expression and its result (True/False),
#    and a last row that checks that <= gives the same as (p or q).
# 4. My two values: "Python" and "python". The result that surprised me:
#    "Python" < "python" is True, even though they are the same word.
#    Python compares text character by character using each character's
#    code number, and the capital "P" (80) has a smaller code than "p" (112),
#    so the capital version counts as "smaller" and comes first.

# Your code below

first = "Python"
second = "python"

comparisons = [
    ("first == second", first == second),
    ("first != second", first != second),
    ("first <  second", first < second),
    ("first >  second", first > second),
    ("first <= second", first <= second),
    ("first >= second", first >= second),
]

p = first < second
q = first == second

combinations = [
    ("p and q", p and q),
    ("p or q", p or q),
    ("not p", not p),
    ("not q", not q),
    ("(first <= second) == (p or q)", (first <= second) == (p or q)),
]

print("Values:", repr(first), "and", repr(second))
print("p = first < second   | q = first == second")
print()
print(f"{'Expression':<32}{'Result':<8}")
print("-" * 40)
for label, result in comparisons + combinations:
    print(f"{label:<32}{str(result):<8}")

print()
print("ord('P') =", ord("P"), "| ord('p') =", ord("p"))