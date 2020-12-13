import netezza_sqlalchemy.netezza_dialect as nzload
import sqlalchemy as alch
import pandas as pd
import make_records as mk
import sql_connect as connection
import csv
import pyspark 
from IPython.display import display
from tableschema import Table, infer, schema

cnxn = connection.cnxn()
cursor = cnxn.cursor()
names_to_insert = ['Jarrell','Amy','Roewan','Caesar','Eevee']
tbl = "DataAnalyst.FamilyNames"
tbl_x_drop = f"IF OBJECT_ID('{tbl}','U') IS NOT NULL DROP TABLE {tbl}"
tbl_x_create = f"""create table {tbl} 
                (id int
                ,name varchar(15)
                ,load_dt datetime default getdate())"""
query = f"select * from {tbl}"

cursor.execute(tbl_x_drop)
cursor.execute(tbl_x_create)
# cursor.execute(tbl_x_insert)
data = cursor.execute(query)

records = mk.new_names(names_to_insert)

for record in records:
  #print(f"{record[0]},{record[1]}") #uncomment to see list of names
  cursor.execute(f"insert into {tbl} (id, name) values({record[0]},'{record[1]}')")

cursor.commit()

# ##Uncomment to view data

# data = pd.read_sql(query,cnxn)
# sql_df = pd.DataFrame(data)
# if sql_df.empty: 
#   print("the dataframe is empty")

# for row in sql_df.itertuples():
#   print(row)

# for col in sql_df.columns:
#   print(col)

#######################CSV to Table Load Using Pandas#######################

csv_fp = r'/home/lozik/CodeProjects/PyProjects/Python4Data/FlatFiles/2m Sales Records.csv'

csv_data = pd.read_csv(csv_fp,sep=",")
csv_df = pd.DataFrame(csv_data)
sql_insert = "INSERT INTO DataAnalyst.2mSalesData VALUES"


list(csv_df.itertuples(index=False, name=None))
  
# i = 0
# for row in csv_df.itertuples():
#   if i > 1000:
#     break
#   print(row)
#   i=i+1
# print(csv_df.dtypes)
# for col in csv_df.columns:
#   print(col)

# print(csv_df.size)
# print(csv_df.ndim)

# CSV options
# infer_schema = "true"
# first_row_is_header = "true"
# delimiter = ","
# file_type = "csv"

#######################CSV to Table Load Using PySpark#######################

# spark = pyspark.sql.SparkSession.builder \
#     .master("local") \
#     .appName("Word Count") \
#     .config("spark.some.config.option", "some-value") \
#     .getOrCreate()

# df = spark.read.format(file_type) \
#   .option("inferSchema", infer_schema) \
#   .option("header", first_row_is_header) \
#   .option("sep", delimiter) \
#   .load(csv_fp)

# #display(df)
# for i in df.dtypes:
#   print(i)


