This project focuses on cleaning, preprocessing, and analyzing employee data using Python libraries NumPy and Pandas.
The dataset contains missing values and duplicate records, which are handled to improve data quality and reliability before performing basic statistical analysis.

🎯 Objective

To transform a raw employee dataset into a clean and structured format by:

Handling missing values
Removing duplicate records
Performing descriptive analysis
Extracting useful business insights
🛠️ Technologies Used

Python
• Pandas – data manipulation and analysis
• NumPy – numerical operations
• Excel (.xlsx) – input and output format

🔄 Data Cleaning Steps Performed

1️⃣ Handling Missing Values

Replaced missing Name, City, Department, and Performance values with "Unknown".
Filled missing Age values using the mean age.
Filled missing Salary values using the average salary.
2️⃣ Removing Duplicates

Duplicate employee records were identified and removed to ensure data consistency.
📈 Data Analysis & Insights

✔ Salary Statistics
Calculated average, minimum, and maximum salary of employees.

✔ Department-Wise Analysis
Counted number of employees per department.

Computed average salary per department.
✔ Location-Wise Analysis

Counted employees based on city.
✔ Top Earners

Identified the top 5 highest-paid employees in the organization.

💾 Output
The cleaned and processed dataset is exported as clean_data.xlsx for further use or reporting.

✅ Key Outcomes
✔ Advantages

• Improved data quality and accuracy
• Demonstrates real-world data cleaning skills
• Useful for HR analytics and reporting
• Beginner-friendly but practical project

❌ Limitations

• No visualization included
• Outlier treatment not implemented

🔮 Future Enhancements

• Add Exploratory Data Analysis (EDA) with charts
• Implement outlier detection
• Add data validation rules
• Integrate visualization using Matplotlib / Seaborn
