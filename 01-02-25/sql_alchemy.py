import pandas as pd
from sqlalchemy import create_engine
import numpy as np

# Replace the following with your database connection details
username = 'root'  # Your MySQL username
password = 'system'  # Your MySQL password
host = 'localhost'  # Your MySQL host, e.g., 'localhost' or an IP address
database = '6774_coe'  # Your MySQL database name

# Create a connection string using SQLAlchemy
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'

# Create an engine
engine = create_engine(connection_string)

# Read data from MySQL into a pandas DataFrame
df_sql = pd.read_sql('SELECT * FROM products', engine)
df_csv = pd.read_csv('orders.csv')
df_excel = pd.read_excel('employee.xltx')

# Display the DataFrame
print('-----SQL TABLE-----')
print(df_sql, '\n')
print("-----CSV FORMAT-----")
print(df_csv, '\n')
print("-----EXCEL FORMAT-----")
print(df_excel, '\n')

merged_df_sql_csv = pd.merge(df_sql, df_csv, on='id', how='outer')
print("-----MERGED FILE (SQL & CSV)-----")
print(merged_df_sql_csv, '\n')

merged_df_sql_csv_excel = pd.merge(merged_df_sql_csv, df_excel, on='customer_name', how='outer')
print("-----MERGED FILE (SQL & CSV & EXCEL)-----")
print(merged_df_sql_csv_excel, '\n')

print('-----Before : Memory Usage for id (int64)-----\n', df_sql['id'].memory_usage(deep=True), '\n')
print(df_sql.dtypes, '\n')
df_sql['id'] = df_sql['id'].astype(np.int16)
print('-----After : Memory for id (int16)-----\n', df_sql['id'].memory_usage(deep=True), '\n')
print(df_sql.dtypes, '\n')

print('-----Before : Memory Usage for id (float64)-----\n', df_sql['price'].memory_usage(deep=True), '\n')
print(df_sql.dtypes, '\n')
df_sql['price'] = df_sql['price'].astype(np.float32)
print('-----After : Memory for id (float32)-----\n', df_sql['price'].memory_usage(deep=True), '\n')
print(df_sql.dtypes, '\n')

'''
OUTPUT:
-----SQL TABLE-----
   id        name   price  quantity
0   1      Laptop  899.99        50
1   2  Smartphone  499.99       120
2   3  Headphones   89.99       200
3   4  Smartwatch  199.99       150
4   5    Keyboard   49.99        80
5   6       Mouse   29.99       120

-----CSV FORMAT-----
   id  customer_name  order_date  total_amount
0   1       John Doe  2025-02-01        999.97
1   2     Jane Smith  2025-02-02        649.98
2   3  Alice Johnson  2025-02-03        229.97
3   4  Michael Brown  2025-02-04       1199.95
4   5    Emily White  2025-02-05        399.99
5   6      David Lee  2025-02-06        799.98
6   7    Chris Green  2025-02-07        359.99
7   8     Kate Adams  2025-02-08        559.95
8   9    Robert King  2025-02-09       1099.89

-----EXCEL FORMAT-----
   employee_id first_name last_name  ...   salary   department  customer_name
0            1       John       Doe  ...   999.97        Sales       John Doe
1            2       Jane     Smith  ...   849.99    Marketing     Jane Smith
2            3     Samuel    Wilson  ...  1099.99  Engineering  Alice Johnson
3            4       Mary   Johnson  ...  1299.99           HR  Michael Brown
4            5      Chris     Brown  ...   799.99        Sales    Emily White
5            6       Anna     Adams  ...  1150.50  Engineering      David Lee
6            7       Paul     White  ...   950.75    Marketing    Chris Green
7            8      Emily       Lee  ...   890.25           HR     Kate Adams
8            9     Robert      King  ...  1200.60        Sales    Robert King

[9 rows x 9 columns]

-----MERGED FILE (SQL & CSV)-----
   id        name   price  quantity  customer_name  order_date  total_amount
0   1      Laptop  899.99      50.0       John Doe  2025-02-01        999.97
1   2  Smartphone  499.99     120.0     Jane Smith  2025-02-02        649.98
2   3  Headphones   89.99     200.0  Alice Johnson  2025-02-03        229.97
3   4  Smartwatch  199.99     150.0  Michael Brown  2025-02-04       1199.95
4   5    Keyboard   49.99      80.0    Emily White  2025-02-05        399.99
5   6       Mouse   29.99     120.0      David Lee  2025-02-06        799.98
6   7         NaN     NaN       NaN    Chris Green  2025-02-07        359.99
7   8         NaN     NaN       NaN     Kate Adams  2025-02-08        559.95
8   9         NaN     NaN       NaN    Robert King  2025-02-09       1099.89

-----MERGED FILE (SQL & CSV & EXCEL)-----
   id        name   price  ...  hire_date   salary   department
0   3  Headphones   89.99  ... 2023-12-11  1099.99  Engineering
1   7         NaN     NaN  ... 2021-09-14   950.75    Marketing
2   6       Mouse   29.99  ... 2022-03-01  1150.50  Engineering
3   5    Keyboard   49.99  ... 2022-07-22   799.99        Sales
4   2  Smartphone  499.99  ... 2024-06-21   849.99    Marketing
5   1      Laptop  899.99  ... 2025-02-01   999.97        Sales
6   8         NaN     NaN  ... 2021-01-20   890.25           HR
7   4  Smartwatch  199.99  ... 2023-08-15  1299.99           HR
8   9         NaN     NaN  ... 2020-12-10  1200.60        Sales

[9 rows x 15 columns]

-----Before : Memory Usage for id (int64)-----
 176

id            int64
name         object
price       float64
quantity      int64
dtype: object

-----After : Memory for id (int16)-----
 140

id            int16
name         object
price       float64
quantity      int64
dtype: object

-----Before : Memory Usage for id (float64)-----
 176

id            int16
name         object
price       float64
quantity      int64
dtype: object

-----After : Memory for id (float32)-----
 152

id            int16
name         object
price       float32
quantity      int64
dtype: object


Process finished with exit code 0
'''