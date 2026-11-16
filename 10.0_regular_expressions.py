"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

import csv
import os
import re

# 1. In: Three pieces of text typed by the user: an email, a postal code
#    and a campaign code. A list of nine test values is also written in the
#    code (one that must pass and two that must fail, for each field).
# 2. Process: Each value is compared with a pattern using re.fullmatch(),
#    which only says True if the WHOLE text follows the pattern. A function
#    per field returns True or False. The three results are combined with
#    "and": the data is saved only if all three are True. Otherwise the
#    program says which fields failed and saves nothing.
# 3. Out: The results of the nine tests, then for the real input a message
#    per failed field, or "Saved" and one new row in validated_data.csv
#    with the columns email, postal_code, campaign_code.
# 4. My three fields and their rules, in plain English (written BEFORE the
#    patterns):
#    - Email: some letters, digits or . _ + - ; then one @ ; then a domain
#      of letters, digits or dashes with at least one dot; and the last
#      part after the final dot has at least 2 letters. Rejected: spaces,
#      no @, no dot after the @. Borderline case: "anna@example" is
#      technically possible inside a company network, but I reject it
#      because every customer address I need has a dot in its domain.
#    - Postal code: exactly 5 digits, nothing before or after.
#    - Campaign code: 3 capital letters, a dash, 4 digits (the year), a
#      dash, 2 digits (the number of the campaign that year).
#      Example: SPR-2027-01. Lowercase is rejected on purpose, so that the
#      same campaign is never saved under two spellings.

# Your code below

EMAIL_PATTERN = r"[A-Za-z0-9._+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
POSTAL_PATTERN = r"[0-9]{5}"
CAMPAIGN_PATTERN = r"[A-Z]{3}-[0-9]{4}-[0-9]{2}"
OUTPUT_FILE = "validated_data.csv"


def is_valid_email(text):
    return re.fullmatch(EMAIL_PATTERN, text) is not None


def is_valid_postal_code(text):
    return re.fullmatch(POSTAL_PATTERN, text) is not None


def is_valid_campaign_code(text):
    return re.fullmatch(CAMPAIGN_PATTERN, text) is not None


# Nine tests: (field, function, value, expected result)
tests = [
    ("email", is_valid_email, "anna.smith+promo@mail.example.com", True),
    ("email", is_valid_email, "anna@example", False),
    ("email", is_valid_email, "anna smith@mail.com", False),
    ("postal code", is_valid_postal_code, "75008", True),
    ("postal code", is_valid_postal_code, "7500", False),
    ("postal code", is_valid_postal_code, "75O08", False),  # letter O, not zero
    ("campaign code", is_valid_campaign_code, "SPR-2027-01", True),
    ("campaign code", is_valid_campaign_code, "spr-2027-01", False),
    ("campaign code", is_valid_campaign_code, "SPR-27-01", False),
]

print("--- Nine tests ---")
correct = 0
for field, function, value, expected in tests:
    result = function(value)
    if result == expected:
        correct = correct + 1
    print(f"{field:<14}{value!r:<38}expected {expected!s:<6} got {result}")
print("Tests as expected:", correct, "out of", len(tests))

# The real program
print()
print("--- Enter your data ---")
email = input("Email: ")
postal_code = input("Postal code: ")
campaign_code = input("Campaign code (like SPR-2027-01): ")

email_ok = is_valid_email(email)
postal_ok = is_valid_postal_code(postal_code)
campaign_ok = is_valid_campaign_code(campaign_code)

if email_ok and postal_ok and campaign_ok:
    is_new_file = not os.path.exists(OUTPUT_FILE)
    with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if is_new_file:
            writer.writerow(["email", "postal_code", "campaign_code"])
        writer.writerow([email, postal_code, campaign_code])
    print("Saved to", OUTPUT_FILE)
else:
    print("Nothing saved. Problems found:")
    if not email_ok:
        print("- Email: needs text, one @, and a domain with a dot (like mail.com).")
    if not postal_ok:
        print("- Postal code: must be exactly 5 digits.")
    if not campaign_ok:
        print("- Campaign code: must look like SPR-2027-01 (3 capitals, year, number).")