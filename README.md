Student Performance Analytics System
Developed by: Anuj Sharma
Internship: Python with AI
Organization: EWB EDU Private Limited (EWB Courses)

1. Project Objective
The Student Performance Analytics System is a Python-based project developed to analyze student academic performance. It processes student records, calculates total and average marks, assigns grades, determines pass/fail status, and generates useful class-level and subject-wise performance summaries.

2. Technologies Used
Python: Core programming logic, loops, conditions, and functions.
NumPy: Numerical calculations and statistical analysis.
Pandas: Loading, processing, sorting, and exporting student data.
CSV: Storing the input dataset and generated results.
Visual Studio Code: Development and execution environment.
3. Dataset Description
The project uses students.csv, which contains 20 sample student records.

The dataset includes the following fields:

Student ID
Name
Department
Python marks
Mathematics marks
AI marks
Electronics marks
English marks
Attendance
The program processes these records and generates student_results.csv, containing the student data along with calculated totals, averages, grades, and results.

4. Implementation
The project is implemented through the following steps:

Load the student dataset using Pandas.
Select the subject columns for performance analysis.
Calculate each student's total and average marks using reusable functions.
Assign grades based on average marks.
Determine pass/fail status using the implemented conditions.
Calculate class-level statistics, including average, highest average, and lowest average.
Calculate subject-wise average marks and identify the best-performing subject.
Sort students by average marks and display the top five performers.
Export the processed student records to student_results.csv.
5. Key Features
Student-wise total and average marks calculation
Automatic grade assignment
Pass/fail evaluation
Class average, highest average, and lowest average
Passed and failed student count
Overall pass percentage
Subject-wise performance analysis
Identification of the best-performing subject
Top five performers based on average marks
Automatic CSV report generation
6. Grading and Pass/Fail Criteria
Grades are assigned according to the student's average marks.

Average Marks	Grade
90 and above	A+
80 to below 90	A
70 to below 80	B
60 to below 70	C
50 to below 60	D
Below 50	F
Pass criteria:

A student must satisfy both of the following conditions to pass:

Average marks must be at least 40.
Marks in every subject must be at least 33.
If either condition is not satisfied, the student is marked as Fail.

7. Project Screenshots
7.1 Program Output and Class Statistics
<img width="1920" height="1080" alt="project-output 1 png" src="https://github.com/user-attachments/assets/8989d2d1-21aa-424c-b061-e1230f49b705" />

7.2 Subject-wise Analysis and Top Performers
<img width="1920" height="1080" alt="project-output 2 png" src="https://github.com/user-attachments/assets/bacb9952-ecd5-4d8e-b5d9-04c3f6c15c99" />

7.3 Student Results
<img width="1920" height="1080" alt="student-results png" src="https://github.com/user-attachments/assets/efc351e3-b314-4d92-a370-14e5c7e9fb8e" />

7.4 main.py Code screenshots
<img width="1920" height="1080" alt="main-code 1 png" src="https://github.com/user-attachments/assets/2e4317e3-3b3b-4218-a6ad-9855f68c3fae" />
<img width="1920" height="1080" alt="main-code 2 png" src="https://github.com/user-attachments/assets/b0a6e50e-f909-4c84-a753-f8ec35340aae" />
<img width="1920" height="1080" alt="main-code 3 png" src="https://github.com/user-attachments/assets/e1ab3aa1-99e0-4216-baa7-0b2627d44873" />


8. How to Run the Project
Prerequisites: Python 3 must be installed on your system.

Step 1: Clone the repository

git clone (https://github.com/anuj2243sharma1102-ux/Student-Performance-Analytics-System)
Step 2: Open the project directory

cd Student-Performance-Analytics
Step 3: Install the required libraries

python -m pip install numpy pandas
Step 4: Run the program

python main.py
After successful execution, the program displays the student performance analysis and generates student_results.csv.

9. Project Files
main.py — Main program for student performance analysis.
functions.py — Reusable functions for calculations and result evaluation.
students.csv — Input student dataset.
student_results.csv — Generated student results report.
README.md — Project overview and instructions.
Student_Performance_Analytics_Documentation_With_Screenshots.pdf — Detailed project documentation.
10. Final Outcome
The project successfully processes 20 sample student records and generates student-wise results, class-level statistics, subject-wise analysis, and a top-five performers report.

In the captured execution, the class average is 70.68, the highest student average is 93.0, the lowest student average is 36.0, and the overall pass percentage is 95%.

11. Learning Outcomes
This project provided practical experience in:

Python programming and conditional logic
Reading and processing CSV files
Working with Pandas DataFrames
Performing numerical calculations with NumPy
Creating reusable functions
Sorting and analyzing student records
Generating structured reports
Publishing a project on GitHub


12. GitHub Repository
Student Performance Analytics System — GitHub Repository
https://github.com/anuj2243sharma1102-ux/Student-Performance-Analytics-System

Developed by Anuj Sharma
Python with AI Internship — EWB EDU Private Limited
