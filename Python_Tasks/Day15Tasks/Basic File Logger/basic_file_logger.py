# 4. Basic File Logger
#Scenario: A system logs user actions.
#Task:
# ● Take user input
# ● Store logs in a file
# ● Use loop to allow multiple entries
# ● Handle file errors using exception handling

try:
    file = open("activity.log", "a")

    while True:
        action = input("Enter user action (type 'exit' to stop): ")

        if action.lower() == "exit":
            break

        file.write(action + "\n")

    file.close()

    print("Logs saved successfully.")

except Exception as e:
    print("File error:", e)