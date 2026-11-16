"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Nothing typed by the user. The program starts from the list of
#    8 monthly budgets (euros) copied from exercise 4.0, plus a limit in percent (my decision: 30).
# 2. Process, function by function: Process, in order:
#    - total_budget(budgets): adds up all the budgets of a list.
#    - highest_budget(budgets): finds the largest budget of a list.
#    - share_of_total(part, total): computes what percent one amount is of a total.
#    - is_budget_concentrated(budgets, limit_percent): calls the three
#      functions above to answer one question (see 4).
# 3. Out:Every function RETURNS its result (numbers, True/False, or None
#    when there is no valid answer). Only the lines at the bottom print.
# 4. The question my fourth function answers: The fourth function answers: "Does the biggest channel take more than
#    the limit share of the total budget?" Splitting it into three makes it
#    easier to check because each small function can be tested alone with a
#    tiny list I can calculate in my head. If the final answer is wrong, I
#    know which of the three to look at, instead of searching through one long block of code.

# One job per function (described without the word "and"):
#    total_budget       -> adds up the budgets of a list.
#    highest_budget     -> finds the largest budget of a list.
#    share_of_total     -> turns an amount into a percent of a total.
#    is_budget_concentrated -> says whether the biggest channel is above the limit.

# Your code below

monthly_budgets = [1200, 450, 800, 300, 2500, 650, 150, 950]
LIMIT_PERCENT = 30


def total_budget(budgets):
    return sum(budgets)


def highest_budget(budgets):
    if len(budgets) == 0:
        return None
    return max(budgets)


def share_of_total(part, total):
    if total == 0:
        return None
    return part / total * 100


def is_budget_concentrated(budgets, limit_percent):
    if len(budgets) == 0:
        return None
    biggest = highest_budget(budgets)
    total = total_budget(budgets)
    share = share_of_total(biggest, total)
    if share is None:  # total is 0, so there is no share to compare
        return None
    return share > limit_percent

print("Test 1 - total_budget:", total_budget([1200, 450, 800]))

print("Test 2 - highest_budget:", highest_budget([1200, 450, 800]))

print("Test 3 - share_of_total:", share_of_total(50, 200))

print("Concentrated with limit 30%:", is_budget_concentrated(monthly_budgets, 30))

print("Concentrated with limit 40%:", is_budget_concentrated(monthly_budgets, 40))

print("Empty list:", is_budget_concentrated([], LIMIT_PERCENT))
