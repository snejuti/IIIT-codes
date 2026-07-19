#FIND EMPLOYESS EARNING ABOVE THEIR DESIGNATION AVERAGE SALARY
#DISPLAY THE TOP 10 HIGHEST PAID EMPLOYEES
import pandas as pd
df = pd.read_csv("file.csv/Employees_1000.csv")
average_salary_by_designation = df.groupby("Designation")["Salary"].mean()  # to calculate average salary for each designation
employees_above_average = df[df.apply(lambda x: x["Salary"] > average_salary_by_designation[x["Designation"]], axis=1)]  # to find employees earning above their designation average salary
print(employees_above_average)  # to print employees earning above their designation average salary 