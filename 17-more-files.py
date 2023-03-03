from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these 2 on a single line of code.
# in_file = open(from_file)
# indata = in_file.read()

in_file2 = open(from_file).read()

# print(f"The input file is {len(indata)} bytes long")
print(f"The input file is {len(in_file2)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
print(f"Outfile type: ", type(out_file))
# out_file.write(indata)
out_file.write(in_file2)
out_file.close()
print(f"in_file2 Type: ", type(in_file2))
print("from_file contents: ", from_file)
print("from_file type: ", type(from_file))
print(f"Outfile type: ", type(out_file))

# Whole script on 1 line