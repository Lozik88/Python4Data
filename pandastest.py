import pyodbc as odbc
import pandas as pd
import numpy as np
import sql_connect as connection
import matplotlib
import math
# Use this doc as a reference for pandas usage
# https://docs.microsoft.com/en-us/sql/machine-learning/data-exploration/python-dataframe-sql-server?view=sql-server-ver15
# insert data from csv file into dataframe.
# working directory for csv file: type "pwd" in Azure Data Studio or Linux
# working directory in Windows c:\users\username
df = pd.read_csv(r'/home/lozik/CodeProjects/PyProjects/Python4Data/FlatFiles/2m Sales Records.csv')
create_tbl = "create table dbo.[2m_sales] ("

for col in df.columns:
    if df[col].dtype == "object":
        char_length = math.ceil(df[col].str.len().max()*1.25)
        str_char_len = str(char_length)
        print(col,char_length,df[col].dtype) 
        create_tbl = create_tbl + "["+col+"]"+" "+"varchar("+str_char_len+"),"
    elif df[col].dtype == "float64":
         print(col,"float")
         create_tbl = create_tbl + "["+col+"] int,"
    elif df[col].dtype == "int64":
         print(col,"int")
         create_tbl = create_tbl + "["+col+"] float,"
    else:
        print(col,df[col].dtype)
create_tbl = create_tbl[:-1]+")"
print(create_tbl)

cnxn = connection.cnxn()
cursor = cnxn.cursor()
# cursor.execute(create_tbl)
# cursor.commit()


df.to_sql("2m_sales") ##this needs a sql alchemy connection