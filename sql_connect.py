import pyodbc as odbc
import sys
def cnxn():

    cnxn = odbc.connect('Driver={/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.6.so.1.1};'
                        #'Server=ENT-PC\SQLEXPRESS;'
                        'Server=192.168.0.36,1433;'
                        'Database=AdventureWorks2017;'
                        'UID=Lozyk;'
                        'PWD=xerxes;'
                        #'Trusted_Connection=yes;'
                        )
    return cnxn
x = cnxn()
x.cursor()
print(sys.executable)