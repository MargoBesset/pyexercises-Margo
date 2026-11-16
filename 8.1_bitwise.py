"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Nothing typed by the user. Permissions are written in the code as
#    bits: each permission is one bit (a power of 2) in a single number.
#    Two campaign roles are defined by hand: an intern and an editor.
# 2. Process, in order:
#    - Combine the intern's and the editor's permissions with | (OR): the
#      result has every bit that is set in at least one of them.
#    - Test whether PUBLISH is present with & (AND): if the result of
#      "permissions & PUBLISH" is not 0, the bit is set.
#    - Add DELETE with |= (turns the bit on, and does nothing if already on).
#    - Remove EDIT with &= ~EDIT (turns the bit off, and does nothing if
#      already off).
#    At each step the value is shown in binary so I can read the bits.
# 3. Out: For each step, the number in decimal and in binary (4 bits), and
#    the answer to the test (True/False).
# 4. My permissions are about who may do what with a marketing campaign:
#    VIEW    (bit 0, value 1): see the campaign and its figures.
#    EDIT    (bit 1, value 2): change the text, budget and audience.
#    PUBLISH (bit 2, value 4): launch the campaign and spend real money.
#    DELETE  (bit 3, value 8): remove the campaign for good.
#    Why bits: one small number holds all four yes/no answers, and
#    combining or testing roles needs a single operation.


# Your code below

VIEW = 0b0001     # 1
EDIT = 0b0010     # 2
PUBLISH = 0b0100  # 4
DELETE = 0b1000   # 8


def show(label, value):
    print(f"{label:<34}{value:>2} = {value:04b}")


intern = VIEW
editor = VIEW | EDIT

show("intern", intern)
show("editor", editor)

combined = intern | editor
show("combined (intern | editor)", combined)

can_publish = (combined & PUBLISH) != 0
print("Can the combined role publish?", can_publish)

combined = combined | PUBLISH
show("after adding PUBLISH", combined)
print("Can it publish now?", (combined & PUBLISH) != 0)

combined = combined & ~EDIT
show("after removing EDIT", combined)
print("Can it still edit?", (combined & EDIT) != 0)
