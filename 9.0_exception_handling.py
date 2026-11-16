"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Text typed by the user, one answer per attempt, to the question
#    "Enter a number to divide 100 by". The "something" I divide is 100.
# 2. Process: A while loop asks up to 3 times. Each answer goes through a
#    try block: float() converts the text, then 100 / number is computed.
#    Two separate except blocks catch the two failures:
#    - ValueError: the text is not a number (for example "abc" or an empty line).
#    - ZeroDivisionError: the number is 0 and division by 0 has no result.
#    The loop stops as soon as one division works, or after 3 attempts.
# 3. Out: The result of 100 / number if it worked, or a message saying
#    that the attempts ran out. Each failed attempt shows its own message.
#    The program always reaches its last line, whatever the user types.
# 4. The two different failures:
#    a) ValueError: the user typed something that is not a number.
#    b) ZeroDivisionError: the user typed 0.
#    They do NOT produce the same message. In a) the user must type a
#    number, in b) the user must type a number other than 0. Telling them
#    the real reason helps them correct it on the next attempt.
#    Maximum number of attempts: 3. When the limit is reached, the program
#    shows a message and ends, so it can never loop for ever.


# Your code below

MAX_ATTEMPTS = 3
DIVIDEND = 100

attempts = 0
result = None

while attempts < MAX_ATTEMPTS and result is None:
    answer = input("Enter a number to divide " + str(DIVIDEND) + " by: ")
    attempts = attempts + 1

    try:
        number = float(answer)
        result = DIVIDEND / number
    except ValueError:
        print("That is not a number. Please type digits, for example 4 or 2.5.")
    except ZeroDivisionError:
        print("You cannot divide by zero. Please type a number other than 0.")

    if result is None and attempts < MAX_ATTEMPTS:
        print("Attempts left:", MAX_ATTEMPTS - attempts)

if result is not None:
    print(DIVIDEND, "/", number, "=", result)
else:
    print("Too many invalid answers. The program stops without a result.")

print("End of the program.")
