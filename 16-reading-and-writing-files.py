'''
Commands for working with files
close
read
readline
truncate
wirte(stuff)
seek(0)
'''

from sys import argv
script, filename = argv

file=argv[1]
print(file)

print(f"We're going to erase {filename}.")
print('If you dont want that, hit CTRL+C (^C).')
print("If you DO want to do that, press ENTER.")

input("?")
print("Opening the file...")
target = open(filename, 'w')
print("Truncating the file. Goodbye.")
#target.truncate()

print("Now I'm going to ask you for 3 lines.")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file. ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("And finally we can close it.")
target.close()

target=open(file, 'r')
print(target.read())
target.close()


#Ugh, i can open this in w+ or r+ mode.
#I can rewirte this my cleaner and shorter later
