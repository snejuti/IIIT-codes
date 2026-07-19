#DISPLAY THE TOP 10 HIGHEST PAID EMPLOYEES
import pandas as pd
df = pd.read_csv("file.csv/Employees_1000.csv")
top_10_employees = df.nlargest(10, "Salary")  # to find the top 10 highest paid employees
print(top_10_employees)  # to print the top 10 highest paid employees