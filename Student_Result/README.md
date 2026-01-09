📌 Project Overview
This project demonstrates data cleaning, preprocessing, and analysis on a student result dataset using Python, Pandas, and NumPy.
The dataset contains missing values, duplicate records, and invalid entries, which are cleaned before performing result analysis such as total marks, grading, and topper identification.

🎯 Objectives

• Clean raw student result data
• Handle missing and invalid values
• Remove duplicate records
• Create derived performance metrics
• Assign grades based on total marks
• Identify top-performing students
• Export cleaned data for further use

🛠️ Technologies Used

1) Python
2) Pandas
3) NumPy
4) Excel (.xlsx)

⚠️ The raw dataset intentionally contains:

1) Missing values (NaN)
2) Duplicate records
3) Invalid values (marks < 0 or > 100)

🧹 Data Cleaning Operations Performed
✔ Handling Missing Values
Filled missing Name and Class with "Unknown"
Filled missing numeric values using column-wise mean

✔ Fixing Invalid Data
Used clip() to restrict marks and attendance between 0 and 100

✔ Removing Duplicates
Duplicate student records were removed using drop_duplicates()

📊 Feature Engineering
🔹 Total Marks

Calculated total marks for each student:
df["Total_Marks"] = df[subjects].sum(axis=1)

🔹 Grade Assignment
Grades were assigned based on total marks using NumPy conditional logic:

Total Marks	Grade
≥ 400	A
300–399	B
200–299	C
100–199	D
< 100	Fail
🏆 Analysis Performed

Sorted students based on Total Marks
Identified Top 3 students
Generated a cleaned and structured dataset

💾 Output

Cleaned dataset exported as:
Cleaned_Student_Data.xlsx

✅ Key Learnings

• Practical use of Pandas for real-world data cleaning
• Efficient NumPy-based conditional logic
• Creating derived columns for analysis
• Sorting and ranking data
• Preparing data for reporting and insights

🚀 Future Improvements (Optional)

• Add Average Marks & Rank
• Perform class-wise analysis
• Add visualizations (Matplotlib / Seaborn)
• Convert project into a Jupyter Notebook

🏁 Conclusion

This project provides hands-on experience with data preprocessing and analysis using Pandas and NumPy, making it a strong beginner-friendly project for data analysis and Python portfolios.
