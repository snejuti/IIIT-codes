#DISPLAY THE FIRST 5 RECORDS
import pandas as pd
df=pd.read_csv("file.csv/Employees_1000.csv")#location and then csv fiel in paranthesis
print(df.head(5))# to print first 5
print(df)# to print all the data


