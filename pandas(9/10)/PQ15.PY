#FIND THE TOP 5 HIGHEST PAID EMPLOYEES IN THE COMPANY
#DISPLAY THE TOP 10 HIGHEST PAID EMPLOYEES
import pandas as pd
df = pd.read_csv("file.csv/Employees_1000.csv")
top_5_employees = df.nlargest(5, "Salary")  # to find the top 5 highest paid employees
print(top_5_employees)  # to print the top 5 highest paid employees