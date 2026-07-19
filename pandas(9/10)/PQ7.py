#DISPLAY UNIQUE DESIGNATIONS IN THE EMPLOYEES_1000.CSV FILE
import pandas as pd
df = pd.read_csv("file.csv/Employees_1000.csv")
unique_Designations = df['Designation'].unique()  # to calculate unique departments
print(unique_Designations)  # to print unique departments
