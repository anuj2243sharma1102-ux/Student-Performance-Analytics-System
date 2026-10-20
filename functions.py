
import numpy as np


def calculate_total(marks):
    """Calculate total marks obtained by a student."""
    return np.sum(marks)


def calculate_average(marks):
    """Calculate average marks of a student."""
    return np.mean(marks)


def assign_grade(average):
    """Assign grade according to average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_result(marks):
    """A student passes if every subject has at least 33 marks
    and the overall average is at least 40."""
    average = calculate_average(marks)

    if average >= 40 and all(mark >= 33 for mark in marks):
        return "Pass"
    else:
        return "Fail"
