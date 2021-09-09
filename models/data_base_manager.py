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

statement = "CREATE TABLE users(id BIGSERIAL PRIMARY KEY, \
            user_name VARCHAR(50) NOT NULL, email VARCHAR(60) NOT NULL,\
            message TEXT NOT NULL UNIQUE, add_time TIMESTAMP NOT NULL);"

# statement = "DROP TABLE users;"

# DELETE FROM records;

cursor.execute(statement)
db.commit()

