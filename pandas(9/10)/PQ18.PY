#COUNT EMPLOYEES IN DIFFERENT SALARY RANGES
#DISPLAY THE TOP 10 HIGHEST PAID EMPLOYEES
import pandas as pd
df = pd.read_csv("file.csv/Employees_1000.csv")
salary_ranges = pd.cut(df["Salary"], bins=[0, 30000, 60000, 90000, 120000, float("inf")], labels=["0-30k", "30k-60k", "60k-90k", "90k-120k", "120k+"])  # to categorize salaries into different ranges
employee_count_by_salary_range = salary_ranges.value_counts()  # to count employees in different salary ranges
print(employee_count_by_salary_range)  # to print the count of employees in different salary ranges