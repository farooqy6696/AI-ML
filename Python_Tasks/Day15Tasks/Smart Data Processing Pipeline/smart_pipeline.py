#9. Smart Data Processing Pipeline
#Scenario: A system processes numeric data from file.
#Task:
# ● Read numbers from a file
# ● Use NumPy for calculations (mean, std)
# ● Convert results to Pandas DataFrame
# ● Use exception handling for bad data
# ● Use a generator to stream data
# ● Apply decorator to measure execution time

import numpy as np
import pandas as pd
import time


# Generator to read numbers from file
def read_numbers(filename):

    try:
        with open(filename, "r") as file:

            for line in file:

                try:
                    yield float(line.strip())

                except ValueError:
                    print("Invalid data:", line.strip())

    except FileNotFoundError:
        print("File not found:", filename)


# Decorator to measure execution time
def measure_time(function):

    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = function(*args, **kwargs)

        end_time = time.time()

        print(
            "\nExecution time:",
            end_time - start_time,
            "seconds"
        )

        return result

    return wrapper


# Main data processing function
@measure_time
def process_data():

    numbers = list(read_numbers("numbers.txt"))

    data = np.array(numbers)

    mean = np.mean(data)

    std = np.std(data)

    df = pd.DataFrame({
        "Number": data
    })

    print("Mean:", mean)

    print("Standard Deviation:", std)

    print("\nDataFrame:")

    print(df)


# Run the program
process_data()