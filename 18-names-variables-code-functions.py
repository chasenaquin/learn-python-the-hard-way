"""
Functions do 3 things
1. They name pieces of code the way variables name strings and numbers.
2. They take arguments the way your scripts take argv
3. using 1 and 2, they let you make your own "mini-scripts" or "tiny-commands"
"""


# This one is like the scripts with argv.
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# *args is pointless, lets do this instead.
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# Takes 1 argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# This one takes 0 arguments
def print_none():
    print("I got nothing.")


print_two("Zed", "Shaw")
print_two_again("Chase", "Burrito")
print_one("First")
print_none()