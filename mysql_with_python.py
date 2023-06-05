import mysql.connector

# Replace the placeholders with your database details
cnx = mysql.connector.connect(
    host='localhost',
    user='username',
    password='ypassword',
    database='database'
)

cursor = cnx.cursor()
# Example: Select all rows from a table
query = "SELECT * FROM table_name"
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Process the results
for row in results:
    # Access the columns of each row
    col1 = row[0]
    col2 = row[1]
    # Do something with the data

# Close the cursor
cursor.close()

cnx.close()
