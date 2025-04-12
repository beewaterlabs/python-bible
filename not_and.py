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

