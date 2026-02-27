# Make the teletext index page
import datetime
import sqlite3
#from createIndex import *
from createIndex2 import *

# Connect to the database connection and get the cursor
connection = sqlite3.connect('teletextai.db')
cursor = connection.cursor()

# Get a list of story titles with their page numbers
cmd = '''SELECT title, pageNumber from story, service
WHERE story.guid=service.guid
ORDER BY pageNumber;
'''
cursor.execute(cmd)
storyList=cursor.fetchall()

#createIndex(storyList) # single page
createIndex2(storyList) # carousel

# close the database connection
connection.close()
print("updateIndex.py finished run at " + str(datetime.datetime.now()))
