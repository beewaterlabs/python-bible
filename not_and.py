#!/usr/bin/env python3

C = 10
D = 5
if C >= 10 and D > 1:
    print("it worked")

if not (C > 10 and D > 1):
    print("it worked")

# And gate only gives true if both conditions are true:
C =10
D = 5
if C >= 10 and D > 1:
    print("wholly molly batman, both conditions are true!")


# not gate only gives true if the condition is false:
if not (C > 10 and D > 1):
    print("it worked")

# not gate only gives true if the condition is false:
if not (C > 100 or D > 100):
    print("it worked")


### OR gate Table:
# A and B: Represent the two input values (0 or 1, which correspond to False or True).
# A OR B: Represents the output of the OR operation. 
# The OR operation is true (1) if at least one of the inputs is true (1). 
# It's only false (0) if both inputs are false (0).

#A | B | A OR B
# ---+---+--------
#  0 | 0 |    0
#  0 | 1 |    1
#  1 | 0 |    1
#  1 | 1 |    1
###
# OR gate only gives true if one of the conditions is true:
# A | B | A OR B
C = 6
D = 2

if (C > 5 and D > 5) or (C > 1 and D > 1):
    print("it worked")