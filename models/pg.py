import psycopg2

PGSQL_URI = "postgresql://avycfqvhbyzvsc:0c0057240a51ced7\
0f3f9163307b97baa967fdf283f26774586c0c8913c7a969@ec2-\
44-196-170-156.compute-1.amazonaws.com:5432/d33s43dhj5grk9"

db = psycopg2.connect(PGSQL_URI)

cursor = db.cursor()

# statement = "CREATE TABLE records(id BIGSERIAL PRIMARY KEY, \
#     query VARCHAR(60) UNIQUE NOT NULL,\
#     add_time TIMESTAMP NOT NULL,\
#     byte_file BYTEA NOT NULL);"

statement = "DROP TABLE queries;"

# DELETE FROM records;

cursor.execute(statement)
db.commit()

