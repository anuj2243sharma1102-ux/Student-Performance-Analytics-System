
import pandas as pd
import numpy as np

from functions import (
    calculate_total,
    calculate_average,
    assign_grade,
    check_result
)

# Step 1: Load student dataset
df = pd.read_csv("students.csv")

subjects = [
    "Python",
    "Mathematics",
    "AI",
    "Electronics",
    "English"
]

# Step 2: Calculate student results
totals = []
averages = []
grades = []
results = []

for index, student in df.iterrows():
    marks = student[subjects].to_numpy(dtype=float)

    total = calculate_total(marks)
    average = calculate_average(marks)

    totals.append(total)
    averages.append(average)
    grades.append(assign_grade(average))
    results.append(check_result(marks))

df["Total"] = totals
df["Average"] = averages
df["Grade"] = grades
df["Result"] = results

# Step 3: Display results
print("\n======================================")
print(" STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("======================================")

print("\nSTUDENT PERFORMANCE REPORT")
print(df[[
    "Student_ID", "Name", "Total",
    "Average", "Grade", "Result"
]].to_string(index=False))

# Step 4: Class statistics
print("\n========== CLASS STATISTICS ==========")

print("Total Students:", len(df))
print("Class Average:", round(np.mean(df["Average"]), 2))
print("Highest Average:", round(np.max(df["Average"]), 2))
print("Lowest Average:", round(np.min(df["Average"]), 2))

passed = (df["Result"] == "Pass").sum()
failed = (df["Result"] == "Fail").sum()

print("Passed Students:", passed)
print("Failed Students:", failed)
print("Pass Percentage:", round(passed / len(df) * 100, 2), "%")

# Step 5: Subject-wise analysis
print("\n========== SUBJECT ANALYSIS ==========")

subject_averages = {}

for subject in subjects:
    average = np.mean(df[subject])
    subject_averages[subject] = average
    print(subject, ":", round(average, 2))

best_subject = max(subject_averages, key=subject_averages.get)
print("\nBest Performing Subject:", best_subject)

# Step 6: Top 5 performers
print("\n========== TOP 5 PERFORMERS ==========")

top_students = df.sort_values(
    by="Average", ascending=False
).head(5)

print(top_students[[
    "Name", "Average", "Grade"
]].to_string(index=False))

# Step 7: Save final report
df.to_csv("student_results.csv", index=False)

print("\nReport saved as student_results.csv")
print("\nProject executed successfully!")
