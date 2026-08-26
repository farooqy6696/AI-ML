file = open("Day8Tasks/article.txt", "r")

content = file.read()

characters = len(content)
words = len(content.split())
lines = len(content.splitlines())

file.close()

print("Number of characters: ", characters)
print("Number of words:", words)
print("Number of lines:", lines)