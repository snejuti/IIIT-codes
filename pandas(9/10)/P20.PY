#WHICH DESIGNATION HAS THE HIGHEST AVERAGE SALARY AND HOW MANY EMPLOYEES ARE IN THAT DESIGNATION
import pandas as pd
df = pd.read_csv("file.csv/Employees_1000.csv") # to read the CSV file containing employee data into a DataFrame
designation_avg_salary = df.groupby("Designation")["Salary"].mean()  # to calculate the average salary for each designation
highest_avg_salary_designation = designation_avg_salary.idxmax()  # to find the designation with the highest average salary
num_employees_in_highest_avg_salary_designation = df[df["Designation"] == highest_avg_salary_designation].shape[0]  # to count the number of employees in the designation with the highest average salary
print(highest_avg_salary_designation)  # to print the designation with the highest average salary
print(num_employees_in_highest_avg_salary_designation)  # to print the number of employees in that designation  