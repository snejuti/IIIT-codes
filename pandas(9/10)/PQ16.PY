#CALCULATE AVERAGE SALARY FOR EACH DESIGNATION IN THE COMPANY
import pandas as pd
df = pd.read_csv("file.csv/Employees_1000.csv")
average_salary_by_designation = df.groupby("Designation")["Salary"].mean()  # to calculate average salary for each designation
print(average_salary_by_designation)  # to print the average salary for each designation