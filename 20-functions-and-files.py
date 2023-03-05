# import argv
from sys import argv
# assign argv variables
script, input_file = argv

# read the file parameter passed in the function
def print_all(f):
    print(f.read())

# This is setting the offset (default is 0 - absolute positioning)
def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("First let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's pring three lines")

current_line = 1
print_a_line(current_line, current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
