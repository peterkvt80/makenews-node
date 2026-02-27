# feed.py
# Reads the RSS feed from url and loads each entry into the teletextai.db database,  
import datetime
import feedparser
import sqlite3

# get the feed
url = 'https://feeds.bbci.co.uk/news/rss.xml?edition=uk'
#url = 'https://feeds.skynews.com/feeds/rss/world.xml'
data = feedparser.parse(url)

# Define database connection and cursor
connection = sqlite3.connect('teletextai.db')
cursor = connection.cursor()

# Remove existing data from the Story table
connection.execute("DELETE FROM Story")

# Put the parsed values into the database
i=0
while i < len(data):
    aguid = data['entries'][i]["guid"]
    atitle = data['entries'][i]["title"]
    adescription = data['entries'][i]["description"]
    adescription = adescription.encode("ascii", "replace").decode("ascii").replace("?", " ") # For now strip out the non ASCII characters and replace with ?. This will be a general Unicode to Teletext function
    # How does it work? It uses decode to add ? where it can't decode. Then replaces it with a space
    alink = data['entries'][i]["link"]
    print('title: ' + atitle + '\n' + 'guid:' + aguid + '\n' + 'link:' + alink + '\n' + 'description:' + adescription)
        
    connection.execute("""INSERT INTO Story(guid, title, description, link) VALUES(?,?,?,?)""", (aguid, atitle, adescription, alink))
    i=i+1

# Print the resulting table    
#cursor.execute("SELECT * FROM Story")
#print(cursor.fetchall())    

# Commit the changes in database and close the connection
connection.commit()
connection.close()

print("feed.py finished run at " + str(datetime.datetime.now()) + "  Processed " + str(len(data)) + " items")
