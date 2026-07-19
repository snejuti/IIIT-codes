#COUNT EMPLOYEES IN EACH DESIGNATION
import pandas as pd
df = pd.read_csv("file.csv/Employees_1000.csv")
df["Designation"].value_counts() # to calculate number of employees in each department
print(df["Designation"].value_counts()) # to print number of employees in each department