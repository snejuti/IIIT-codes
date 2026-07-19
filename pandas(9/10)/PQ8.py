#FIND THE HISGHEST AND LOWEST SALARY IN THE EMPLOYEES_1000.CSV FILE
import pandas as pd
df = pd.read_csv("file.csv/Employees_1000.csv")
print(df["Salary"].max()) # to calculate maximum salary
print(df["Salary"].min() ) # to calculate minimum salary