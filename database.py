import sqlite3

db_connection = sqlite3.connect("users.db")
cursor = db_connection.cursor()

create_query = 'create table if not exist allowed_users (id integer, first_name text, last_name text, username text)'
cursor.execute(create_query)


