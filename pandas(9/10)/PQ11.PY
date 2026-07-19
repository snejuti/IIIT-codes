#DISPLAY EMPLOYEES WHOSE SALARY IS GREATER THAN 100000
import pandas as pd
df = pd.read_csv("file.csv/Employees_1000.csv")
print(df[df["Salary"] > 100000]) # to display employees having salary more than 100000
