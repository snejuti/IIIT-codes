#FIND THE AVERAGE SALARY OF ALL EMPLOYEES IN THE GIVEN CSV FILE
import pandas as pd
df = pd.read_csv("file.csv/Employees_1000.csv")
print(df["Salary"].mean()) # to calculate average salary