import psycopg2

# connect to the default postgres database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="openthedoor"
)

conn.autocommit = True
# create a new database

# connect to the new database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mydatabase",
    user="postgres",
    password="openthedoor"
)

# create a new table
cur = conn.cursor()

# insert data into the table
cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("John Doe", 30))
conn.commit()

# query the table and print results
cur.execute("SELECT id, name, age FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

# close the connection
conn.close()