#2. Notes Reader Program

file = open("Day8Tasks/notes.txt", "r")

content = file.read()

print("Contents of the file:")
print(content)

file.close()