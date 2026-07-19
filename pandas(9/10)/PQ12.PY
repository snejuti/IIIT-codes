#FIND THE AVERAGE SALARY OF EMPLOYEES FOR EACH DESIGNATION
import pandas as pd
df = pd.read_csv("file.csv/Employees_1000.csv")
unique_Designations = df['Designation'].unique()  # to calculate unique departments
for i in unique_Designations:
    avg_salary = df[df["Designation"] == i]["Salary"].mean()  # to calculate average salary for each department
    print("Average salary for", i, "is", avg_salary)  # to print average salary for each department