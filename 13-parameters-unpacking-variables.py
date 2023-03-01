#calling argument variable module (library)
from sys import argv
#unpacks the arguments - asigning them to the following variables
script, first, second, third = argv

print("The script you called: ", script)
print("Your first variable is", first)
print("Your second variable is", second)
print("Your third variable is", third)
