#7. Student Result Generator (Method Overloading Concept)

class Result:

    def calculate(self, subject1, subject2, subject3=None):

        if subject3 is None:
            average = (subject1 + subject2)/2
            print("Average of 2 subjects =", average)

        else:
            average = (subject1 + subject2 + subject3)/3
            print("Average of 3 subjects =", average)

student = Result()

student.calculate(80, 90)

student.calculate(80, 90, 100)