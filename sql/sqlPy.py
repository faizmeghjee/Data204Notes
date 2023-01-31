# %%
import pyodbc

# Find the DRIVERS you have available by using the pyodbc.drivers() method
pyodbc.drivers()

print(pyodbc.drivers())

sql_server = 'faizm\LOCALDB#E21E3648'

# Create a VARIABLE to store the connection string
conx_string = "driver={SQL SERVER}; server=faizm\LOCALDB#E21E3648; database=Northwind; trusted_connection=YES;"

# Create a VARIABLE for the sql query
query = 'SELECT * FROM Customers'

print(0)

# Create a CONNECTION using the connection string and pyodbc.connect()
conx = pyodbc.connect(conx_string);

print(1)

# Create a CURSOR that we can use to work in the database
cursor = conx.cursor()

print(2)

# Run the QUERY using cursor.execute()
cursor.execute(query)

print(3)

# Store the RESULTS in a variable
data = cursor.fetchall()

print(4)

# Display the RESULTS to check the data (first 5 rows)
print(data[:5])

print(5)

conx.close()

# %%
