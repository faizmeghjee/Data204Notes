# %%
import pyodbc

print(pyodbc.drivers())
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
docker_Northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = docker_Northwind.cursor()
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
# %% Querying
cust_rows = cursor.execute(
    "SELECT * \
    FROM Customers;"
    ).fetchall()

for record in cust_rows:
    print(record)
print(cust_rows)

# %%
import pandas as pd

customers_df = pd.DataFrame(cust_rows)
customers_df.to_sql(name='df_customers', con=cursor, if_exists='replace')

# %%
import sqlalchemy

server = 'localhost,1433' # or server ip address
database = 'Northwind'
user = 'SA'
password = 'Passw0rd2018'
driver = 'SQL+Server'
engine = sqlalchemy.create_engine(f"mssql+pyodbc://{user}:{password}@{server}/{database}?driver={driver}")

# open a connection using sqlalchemy
connection = engine.connect()
print(connection)
# %% Querying
with engine.connect() as conn:
    a = conn.exec_driver_sql("SELECT * FROM Customers")
    for row in a:
        print(row)
