#7. Generator-based Log Reader
#Scenario: A large log file needs to be processed.
#Task:
# ● Create a generator to read file line by line
# ● Use loop to process logs
# ● Use condition to filter errors
# ● Count occurrences using a dictionary

def read_logs(filename):
    with open(filename, "r") as file:

        for line in file:
            yield line.strip()


error_counts = {}

for log in read_logs("sample.log"):

    if "ERROR" in log:

        error_message = log.split("ERROR: ")[1]

        if error_message in error_counts:
            error_counts[error_message] += 1
        else:
            error_counts[error_message] = 1


print("Error Counts:")

for error, count in error_counts.items():
    print(error, ":", count)