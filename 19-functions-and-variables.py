from sys import argv


def cheese_and_crackers(cheese_count, box_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {box_of_crackers} boxes of crackers!")


print("We can just give the function numbers directly when called inside program.")
cheese_and_crackers(20, 30)

print("Or, we can use variables in our script.")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too...")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math!")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# print("Using arg input...")
# script, amount_of_cheese_arg, amount_of_crackers_arg = argv
# cheese_and_crackers(amount_of_cheese_arg, amount_of_crackers_arg)
