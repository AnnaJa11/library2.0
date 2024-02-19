import sqlite3

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
   except sqlite3.Error as e:
       print(e)
   return conn

def add_author(conn, author):
   """
   Add new author into the authors table
   :param conn:
   :param author:
   :return: author id
   """
   sql = '''INSERT INTO authors(name, surname, genres)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, author)
   conn.commit()
   return cur.lastrowid

def add_book(conn, book):
   """
   Add a new book into the books table
   :param conn:
   :param book:
   :return: book id
   """
   sql = '''INSERT INTO books(auth_id, title, description, release_date)
             VALUES(?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, book)
   conn.commit()
   return cur.lastrowid


def add_availability(conn, aval):
   """
   Add availability status into the availability table
   :param conn:
   :param aval:
   :return: aval id
   """
   sql = '''INSERT INTO availability(book_id, av_status)
             VALUES(?,?)'''
   cur = conn.cursor()
   cur.execute(sql, aval)
   conn.commit()
   return cur.lastrowid


if __name__ == "__main__":
   author = ("Samuel", "Becket ","drama")
   
   conn = create_connection("database.db")
   a_id = add_author(conn, author)

   book = (
       a_id,
       "Waiting for Godot",
       "The story revolves around two seemingly homeless men simply waiting for someone—or something—named Godot.",
       "1949-05-03 00:00:00"
   )

   book_id = add_book(conn, book)
   
   aval = (book_id, "available")
   aval_id = add_availability(conn, aval)

   print(a_id, book_id, aval_id)
   conn.commit()