#FIND THE DESIGNATION WITH THE HIGHEST TOTAL SALARY EXPENSES
import pandas as pd
df = pd.read_csv("file.csv/Employees_1000.csv")
designation_salary_expenses = df.groupby("Designation")["Salary"].sum()  # to calculate the total salary expenses for each designation
highest_expense_designation = designation_salary_expenses.idxmax()  # to find the designation with the highest total salary expenses
print(highest_expense_designation)  # to print the designation with the highest total salary expenses   