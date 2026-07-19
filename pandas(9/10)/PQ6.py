#FIND THE TOTAL NO. OF EMPLOYEES IN THE COMPANY.
import pandas as pd
df = pd.read_csv("file.csv/Employees_1000.csv") 
total_employees = len(df)  # to calculate total number of employees
print(total_employees)  # to print total number of employees