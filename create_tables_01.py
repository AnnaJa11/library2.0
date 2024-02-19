import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

if __name__ == "__main__":

   create_authors_sql = """
   -- authors table
   CREATE TABLE IF NOT EXISTS authors (
      id integer PRIMARY KEY,
      name text NOT NULL,
      surname text NOT NULL,
      genres text NOT NULL
   );
   """

   create_books_sql = """
   -- books table
   CREATE TABLE IF NOT EXISTS books (
      id integer PRIMARY KEY,
      auth_id integer NOT NULL,
      title VARCHAR(250) NOT NULL,
      description TEXT,
      release_date text NOT NULL,
      FOREIGN KEY (auth_id) REFERENCES authors (id)
   );
   """

   create_availability_sql = """
   -- availability table
   CREATE TABLE IF NOT EXISTS availability (
      id integer PRIMARY KEY,
      book_id integer NOT NULL,
      av_status text NOT NULL,
      FOREIGN KEY (book_id) REFERENCES books (id)
   );
   """

   db_file = "database.db"

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_authors_sql)
       execute_sql(conn, create_books_sql)
       execute_sql(conn, create_availability_sql)
       conn.close()