# import libraries
import pandas as pd

# read excel file
emp = pd.read_excel("employee.xlsx")

# check column names
columns = emp.columns

# check data types of columns
# col_info = emp.info()
col_describe = emp.describe()

# looking for missing data
is_null = emp.isnull().sum()       # don't have any missing data here
