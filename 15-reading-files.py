from sys import argv

script, file = argv

txt = open(file)

print(f"Here is the contents of your file: {file}: ")
print(txt.read())

print("Another method: Type file name,")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())

txt.close()
txt_again.close()
