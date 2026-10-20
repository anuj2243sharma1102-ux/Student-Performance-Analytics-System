# Student Performance Analytics System

*Developed by:* Yash Sharma  
*Internship:* Python with AI  
*Organization:* EWB EDU Private Limited (EWB Courses)

## 1. Project Objective

The Student Performance Analytics System is a Python-based project developed to analyze student academic performance. It processes student records, calculates total and average marks, assigns grades, determines pass/fail status, and generates useful class-level and subject-wise performance summaries.

## 2. Technologies Used

- *Python:* Core programming logic, loops, conditions, and functions.
- *NumPy:* Numerical calculations and statistical analysis.
- *Pandas:* Loading, processing, sorting, and exporting student data.
- *CSV:* Storing the input dataset and generated results.
- *Visual Studio Code:* Development and execution environment.

## 3. Dataset Description

The project uses students.csv, which contains 20 sample student records.

The dataset includes the following fields:

- Student ID
- Name
- Department
- Python marks
- Mathematics marks
- AI marks
- Electronics marks
- English marks
- Attendance

The program processes these records and generates student_results.csv, containing the student data along with calculated totals, averages, grades, and results.

## 4. Implementation

The project is implemented through the following steps:

1. Load the student dataset using Pandas.
2. Select the subject columns for performance analysis.
3. Calculate each student's total and average marks using reusable functions.
4. Assign grades based on average marks.
5. Determine pass/fail status using the implemented conditions.
6. Calculate class-level statistics, including average, highest average, and lowest average.
7. Calculate subject-wise average marks and identify the best-performing subject.
8. Sort students by average marks and display the top five performers.
9. Export the processed student records to student_results.csv.

## 5. Key Features

- Student-wise total and average marks calculation
- Automatic grade assignment
- Pass/fail evaluation
- Class average, highest average, and lowest average
- Passed and failed student count
- Overall pass percentage
- Subject-wise performance analysis
- Identification of the best-performing subject
- Top five performers based on average marks
- Automatic CSV report generation

## 6. Grading and Pass/Fail Criteria

Grades are assigned according to the student's average marks.

| Average Marks | Grade |
|---|---|
| 90 and above | A+ |
| 80 to below 90 | A |
| 70 to below 80 | B |
| 60 to below 70 | C |
| 50 to below 60 | D |
| Below 50 | F |

*Pass criteria:*

A student must satisfy both of the following conditions to pass:

- Average marks must be at least 40.
- Marks in every subject must be at least 33.

If either condition is not satisfied, the student is marked as *Fail*.

## 7. Project Screenshots

### 7.1 Program Output and Class Statistics

This screenshot shows the student-wise report, class average, highest and lowest averages, and pass/fail statistics.

![Program Output](screenshots/project-output-1.png)

### 7.2 Subject-wise Analysis and Top Performers

This output displays the average marks of each subject, the best-performing subject, and the top five performers.

![Subject Analysis and Top Performers](screenshots/project-output-2.png)

### 7.3 Generated Student Results

The generated CSV report contains all student records with their calculated performance details.

![Student Results](screenshots/student-results.png)

## 8. How to Run the Project

*Prerequisites:* Python 3 must be installed on your system.

*Step 1: Clone the repository*

bash
git clone https://github.com/YashSharmaECE/student-performance-analytics.git


*Step 2: Open the project directory*

bash
cd student-performance-analytics


*Step 3: Install the required libraries*

bash
python -m pip install numpy pandas


*Step 4: Run the program*

bash
python main.py


After successful execution, the program displays the student performance analysis and generates student_results.csv.

## 9. Project Files

- main.py — Main program for student performance analysis.
- functions.py — Reusable functions for calculations and result evaluation.
- students.csv — Input student dataset.
- student_results.csv — Generated student results report.
- README.md — Project overview and instructions.
- Student_Performance_Analytics_Documentation_With_Screenshots.pdf — Detailed project documentation.

## 10. Final Outcome

The project successfully processes 20 sample student records and generates student-wise results, class-level statistics, subject-wise analysis, and a top-five performers report.

In the captured execution, the class average is 70.68, the highest student average is 93.0, the lowest student average is 36.0, and the overall pass percentage is 95%.

## 11. Learning Outcomes

This project provided practical experience in:

- Python programming and conditional logic
- Reading and processing CSV files
- Working with Pandas DataFrames
- Performing numerical calculations with NumPy
- Creating reusable functions
- Sorting and analyzing student records
- Generating structured reports
- Publishing a project on GitHub

## 12. Project Documentation

The detailed documentation contains the project objective, dataset description, implementation, grading rules, output analysis, and actual program screenshots.

[*View Project Documentation (PDF)*](Student_Performance_Analytics_Documentation_With_Screenshots.pdf)

## 13. GitHub Repository

[*Student Performance Analytics System — GitHub Repository*](https://github.com/YashSharmaECE/student-performance-analytics)

---

*Developed by Yash Sharma*  
Python with AI Internship — EWB EDU Private Limited
