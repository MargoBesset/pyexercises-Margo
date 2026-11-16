"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The function receives one list of budgets (numbers, in euros).
#    The program itself has no typed input: the list comes from exercise 4.0.
# 2. Process: The function adds up all the budgets with sum() and divides
#    by how many there are with len(). If the list is empty, it does not
#    divide (that would crash) and gives back None instead.
# 3. Out: The function RETURNS one number: the average budget. For an empty
#    list it returns None. The program then prints the three results.
# 4. My function name, and why return rather than print: The function is called average_budget. Its name says what it does
#    without reading the code: it gives the average of a list of budgets.
#    A name like "process" or "do_stuff" would say nothing.


# Your code below

monthly_budgets = [1200, 450, 800, 300, 2500, 650, 150, 950]


def average_budget(budgets):
    if len(budgets) == 0:
        return None
    return sum(budgets) / len(budgets)

all_channels = average_budget(monthly_budgets)
first_three = average_budget(monthly_budgets[:3])
last_four = average_budget(monthly_budgets[4:])

print("Average of all 8 channels:", all_channels)
print("Average of the first 3 channels:", first_three)
print("Average of the last 4 channels:", last_four)

print("Average yearly cost of one channel:", all_channels * 12)

#Empty list : 
print("Average of an empty list:", average_budget([]))