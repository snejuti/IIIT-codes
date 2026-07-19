#SORT EMPLOYEES BY SALARY IN DESCENDING ORDER
import pandas as pd
df = pd.read_csv("file.csv/Employees_1000.csv")
sorted_df = df.sort_values(by="Salary", ascending=False)  # to sort employees by salary in descending order
print(sorted_df)  # to print sorted employees by salary in descending order