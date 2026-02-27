# createDB.py
# Run this to set up the database tables initially.
# Note that this will also erase the previous data if it existed
# so you can reset the system for testing.
#
# import the sqlite3 module
import sqlite3

# Define connection and cursor
connection = sqlite3.connect('teletextai.db')
cursor = connection.cursor()

# create tables
cursor.execute("DROP TABLE IF EXISTS Story")
createTable = '''CREATE TABLE Story(
   guid VARCHAR(200) PRIMARY KEY,
   title VARCHAR(100),
   description VARCHAR(500),
   link VARCHAR(100)
)'''
cursor.execute(createTable)
#cursor.execute("INSERT INTO Story VALUES('alpha', 'my caption', 'all about the story', 'http://www.xenoxxx.com')")

# Service are the pages being actually being transmitted
# The hash function is a unique filename for each page
cursor.execute("DROP TABLE IF EXISTS Service")
createTable = '''CREATE TABLE Service(
   guid VARCHAR(200),
   pagenumber int PRIMARY KEY,
   plaintext VARCHAR(10000),
   summary VARCHAR(5000)
)'''
cursor.execute(createTable)

# We will use pages 102 to 119 for news
with connection:
  cur = connection.cursor()
  # Probably a better way to do this
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(102, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(103, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(104, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(105, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(106, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(107, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(108, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(109, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(110, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(111, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(112, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(113, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(114, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(115, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(116, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(117, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(118, NULL, NULL, NULL)")
  cur.execute("INSERT INTO Service(PageNumber, guid, plaintext, summary) VALUES(119, NULL, NULL, NULL)")

# check the database creation data
if cursor:
    print("Database Created Successfully !")
else:
    print("Database Creation Failed !")

# Commit the changes in database and Close the connection
connection.commit()
connection.close()