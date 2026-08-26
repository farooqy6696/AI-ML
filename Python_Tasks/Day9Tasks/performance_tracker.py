#14. Performance Tracker (Decorators)

import time


def calculate_time(func):

    def wrapper():
        start = time.time()

        func()

        end = time.time()

        print("Execution Time:", end - start, "seconds")

    return wrapper


@calculate_time
def report():
    print("Generating Report...")
    time.sleep(2)
    print("Report Generated")


report()